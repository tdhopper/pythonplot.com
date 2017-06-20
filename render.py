#!/usr/local/bin/python
# encoding=utf8

import json
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader
import re
import markdown

md = markdown.Markdown(extensions=['meta'])

packages = {
    "ggplot": "ggplot2 (R)",
    "pandas": "Pandas",
    "matplotlib": "Matplotlib",
    "plotnine": "plotnine",
}

names = {
    "bar-counts": "Basic Bar Chart",
    "simple-histogram": "Basic Histogram",
    "scatter-plot": "Basic Scatter Plot",
    "scatter-plot-with-colors": "Scatter Plot with Colored Points by Category",
    "scatter-plot-with-size": "Scatter Plot with Points Sized by Continuous Value",
    "scatter-plot-with-facets": "Scatter Plot Faceted on Two Variables",
    "scatter-plot-with-facet": "Scatter Plot Faceted on One Variables",
}

with open("INTRO.md", "r") as f:
    intro = f.read()


def image_from_cell(cell):
    return cell['outputs'][0]['data']['image/png'].replace("\n", "").strip()


def source_from_cell(cell):
    source = "".join(cell['source']).strip()
    if "%%R" in source:
        source = '\n'.join(source.split('\n')[1:])
    if source.startswith('"""') or source.startswith("'''"):
        m = re.match("(?:[\"']{3,})((?:.|\n)*)(?:[\"']{3,})((?:.|\n)*)", source, re.MULTILINE)
        return m.groups()
    return "", source


def extract_cells():
    with open("./ggplot vs Python Plotting.ipynb", 'r') as f:
        nb = json.load(f)
    cells = nb['cells']
    tags = {i: set(c['metadata'].get('tags') or {}) for i, c in enumerate(cells)}

    meta = defaultdict(list)
    for cell_num, tags in tags.items():
        if 'ex' not in tags:
            continue
        tags = {t.split(":")[0]: t.split(":")[1] for t in tags if ":" in t}

        comment, source = source_from_cell(cells[cell_num])
        image = image_from_cell(cells[cell_num])

        meta[(names.get(tags['name'], tags['name']), tags['name'])].append({
            "cell_num": cell_num,
            "package": packages.get(tags["package"], tags["package"]),
            "package-slug": tags['package'],
            "image": image,
            "content": source,
            "comment": md.convert(comment) or None,
        })
    meta = {k: v[::-1] for k, v in meta.items()}
    return meta


output = defaultdict(list)

if __name__ == '__main__':
    plots = extract_cells()

    env = Environment(loader=FileSystemLoader('web'), extensions=['jinja2_highlight.HighlightExtension'])
    template = env.get_template('t_index.html')
    output_from_parsed_template = template.render(intro=md.convert(intro), plots=plots)


    # to save the results
    with open("web/index.html", "w") as fh:
        fh.write(output_from_parsed_template)
