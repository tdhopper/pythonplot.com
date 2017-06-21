#!/usr/local/bin/python
# encoding=utf8

import json
from jinja2 import Environment, FileSystemLoader
from collections import defaultdict
import re
import markdown
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
md = markdown.Markdown(extensions=['meta', 'footnotes'])

packages = {
    "pandas": "Pandas",
    "matplotlib": "Matplotlib",
    "seaborn": "Seaborn",
    "plotnine": "plotnine",
    "ggplot": "ggplot2 (R)",
}

names = {
    "bar-counts": "Bar Chart",
    "simple-histogram": "Histogram",
    "scatter-plot": "Scatter Plot",
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
                return c['data']['image/png'].replace("\n", "").strip()
    except KeyError as e:
        logging.error("Can't find image in cell: %s", cell['source'])
        raise e


def source_from_cell(cell):
    source = "".join(cell['source']).strip()
    source = source.replace(";", "")
    if "%%R" in source:
        source = '\n'.join(source.split('\n')[1:])
    else:
        source = source.replace('"', "'")
    if source.startswith('"""') or source.startswith("'''"):
        m = re.match("(?:[\"']{3,})((?:.|\n)*)(?:[\"']{3,})((?:.|\n)*)", source, re.MULTILINE)
        return m.groups()
    return "", source


def tags_from_cell(cell):
    tags = set(cell['metadata'].get('tags') or {})
    if "ex" in tags:
        return {t.split(":")[0]: t.split(":")[1] for t in tags if ":" in t}


def reorder_meta(meta):
    def order_plots(plots):
        if plots:
            return sorted(plots, key=lambda k: list(packages.keys()).index(k['package-slug']))
        else:
            return plots
    meta = {(name, slug): order_plots(meta[slug]) for slug, name in names.items()}
    return meta


def extract_cells():
    with open("./ggplot vs Python Plotting.ipynb", 'r') as f:
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


if __name__ == '__main__':
    plots = extract_cells()

    env = Environment(loader=FileSystemLoader('web'), extensions=['jinja2_highlight.HighlightExtension'])
    template = env.get_template('t_index.html')
    output_from_parsed_template = template.render(intro=md.convert(intro), plots=plots)


    # to save the results
    with open("web/index.html", "w") as fh:
        fh.write(output_from_parsed_template)
