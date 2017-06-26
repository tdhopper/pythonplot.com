#!/usr/local/bin/python
# encoding=utf8

import sys
import json
from jinja2 import Environment, FileSystemLoader
from collections import defaultdict
import re
import markdown
import logging
import subprocess
import base64
import hashlib


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
md = markdown.Markdown(extensions=['meta', 'footnotes'])

packages = {
    "pandas": "Pandas",
    "matplotlib": "Matplotlib",
    "seaborn": "Seaborn",
    "plotnine": "plotnine",
    "ggplot": "ggplot2 (R)",
    "bokeh": "Bokeh",
}

names = {
    "bar-counts": "Bar Chart",
    "simple-histogram": "Histogram",
    "scatter-plot": "Scatter Plot",
    "timeseries": "Time Series",
    "scatter-plot-with-colors": "Scatter Plot with Faceted with Color",
    "scatter-plot-with-size": "Scatter Plot with Points Sized by Continuous Value",
    "scatter-plot-with-facet": "Scatter Plot Faceted on One Variable",
    "scatter-plot-with-facets": "Scatter Plot Faceted on Two Variables",
    "scatter-with-regression": "Scatter Plot and Regression Line with 95% Confidence Interval Layered",
    "stacked-smooth-line-and-scatter": "Smoothed Line Plot and Scatter Plot Layered",
    "stacked-bar-chart": "Stacked Bar Chart",
    "dodged-bar-chart": "Dodged Bar Chart",
    "stacked-kde": "Stacked KDE Plot",
}

with open("INTRO.md", "r") as f:
    intro = f.read()


def image_from_cell(cell):
    try:
        for c in cell['outputs']:
            if 'data' in c and 'image/png' in c['data']:
                base64_img = c['data']['image/png'].replace("\n", "").strip()
                filename = hashlib.md5()
                filename.update(base64_img.encode('ascii'))
                web_path = "/img/plots/{}.png".format(filename.hexdigest())
                full_path = "web" + web_path
                with open(full_path, "wb") as fh:
                    fh.write(base64.b64decode(base64_img))
                return web_path
    except KeyError as e:
        logging.error("Can't find image in cell: %s", cell['source'])
        raise e
    raise Exception("Can't find an image in cell %s", cell['source'])


def source_from_cell(cell):
    source = "".join(cell['source']).strip()
    source = source.replace(";", "")
    source = source.replace("Image(export_png(p))", "") # remove bokeh render
    if "%%R" in source:
        source = '\n'.join(source.split('\n')[1:])
    else:
        source = source.replace('"', "'")
    if source.startswith('"""') or source.startswith("'''"):
        m = re.match("(?:[\"']{3,})((?:.|\n)*)(?:[\"']{3,})((?:.|\n)*)", source, re.MULTILINE)
        return m.groups()
    return "", source


def tags_from_cell(cell, type='ex'):
    tags = set(cell['metadata'].get('tags') or {})
    if type in tags:
        return {t.split(":")[0]: t.split(":")[1] for t in tags if ":" in t}


def data_from_cell(cell):
    classes = "table table-sm table-striped table-responsive table-bordered"
    try:
        for c in cell['outputs']:
            if 'data' in c and 'text/html' in c['data']:
                table = ' '.join(c['data']['text/html'])
                table = table.replace('border="1" class="dataframe"', 'class="{}"'.format(classes))
                table = table.replace('<thead>', '<thead class="thead-inverse">')
                return table
    except KeyError as e:
        logging.error("Can't find data in cell: %s", cell['source'])
        raise e
    raise Exception("Can't find an dataset in cell %s", cell['source'])


def reorder_meta(meta):
    def order_plots(plots):
        if plots:
            return sorted(plots, key=lambda k: list(packages.keys()).index(k['package-slug']))
        else:
            return plots
    meta = {(name, slug): order_plots(meta[slug]) for slug, name in names.items()}
    return meta


def extract_data(path):
    with open(path, 'r') as f:
        nb = json.load(f)
    cells = nb['cells']
    full_data = {}
    tags = {i: tags_from_cell(c, type='data') for i, c in enumerate(cells)}
    for cell_num, tags in tags.items():
        if tags is None:
            continue
        data = data_from_cell(cells[cell_num])
        full_data[tags['name']] = data
    return full_data


def extract_cells(path):
    with open(path, 'r') as f:
        nb = json.load(f)
    cells = nb['cells']
    tags = {i: tags_from_cell(c) for i, c in enumerate(cells)}

    meta = defaultdict(list)
    for cell_num, tags in tags.items():
        if tags is None:
            continue
        comment, source = source_from_cell(cells[cell_num])
        image = image_from_cell(cells[cell_num])

        meta[tags['name']].append({
            "cell_num": cell_num,
            "package": packages.get(tags["package"], tags["package"]),
            "package-slug": tags['package'],
            "image": image,
            "content": source,
            "comment": md.convert(comment) or None,
        })
    meta = reorder_meta(meta)

    return meta


def get_git_revision_short_hash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip().decode("utf8")


if __name__ == '__main__':
    plots = extract_cells(sys.argv[1])
    data = extract_data(sys.argv[1])

    env = Environment(loader=FileSystemLoader('templates'), extensions=['jinja2_highlight.HighlightExtension'])
    template = env.get_template('t_index.html')
    output_from_parsed_template = template.render(intro=md.convert(intro),
                                                  plots=plots,
                                                  git=get_git_revision_short_hash(),
                                                  data=data)


    # to save the results
    with open("web/index.html", "w") as fh:
        fh.write(output_from_parsed_template)
