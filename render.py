import json
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader


packages = {
    "ggplot": "ggplot2 (R)",
    "pandas": "Pandas",
}

names = {
    "bar-counts": "Basic Bar Chart",
    "simple-histogram": "Basic Histogram",
    "scatter-plot": "Basic Scatter Plot",
}

def get_source_and_image(num, cells):
    image = cells[num]['outputs'][0]['data']['image/png'].replace("\n", "").strip()
    source = "".join(cells[num]['source']).strip()
    if "%R" in source:
        source = '\n'.join(source.split('\n')[1:])
    return source, image


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

        source = "".join(cells[cell_num]['source']).strip()
        if "%R" in source:
            source = '\n'.join(source.split('\n')[1:])
        image = cells[cell_num]['outputs'][0]['data']['image/png'].replace("\n", "").strip()

        meta[(names.get(tags['name'], tags['name']), tags['name'])].append({
            "cell_num": cell_num,
            "package": packages.get(tags["package"], tags["package"]),
            "package-slug": tags['package'],
            "image": image,
            "content": source,
        })
    meta = {k: v[::-1] for k, v in meta.items()}
    return meta


output = defaultdict(list)

if __name__ == '__main__':
    plots = extract_cells()

    env = Environment(loader=FileSystemLoader('web'), extensions=['jinja2_highlight.HighlightExtension'])
    template = env.get_template('t_index.html')
    output_from_parsed_template = template.render(foo=output, plots=plots)


    # to save the results
    with open("web/index.html", "w") as fh:
        fh.write(output_from_parsed_template)
