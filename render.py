import json
import pandas as pd
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader


def get_source_and_image(num, cells):
    image = cells[num]['outputs'][0]['data']['image/png'].replace("\n", "").strip()
    source = "".join(cells[num]['source']).strip()
    if "%R" in source:
        source = '\n'.join(source.split('\n')[1:])
    return source, image




if __name__ == '__main__':

    with open("./ggplot vs Python Plotting.ipynb", 'r') as f:
        nb = json.load(f)
    cells = nb['cells']
    tags = {i: set(c['metadata'].get('tags') or {}) for i, c in enumerate(cells)}

    meta = defaultdict(list)
    for cell_num, tags in tags.items():
        if 'ex' not in tags:
            continue
        tags = {t.split(":")[0]: t.split(":")[1] for t in tags if ":" in t}
        print(tags['name'])
        meta[tags['name']].append({
            "cell_num": cell_num,
            "package": tags["package"],
        })

    output = [
        ["Bar Plot of Counts", "ggplot", *get_source_and_image(6, cells)],
        ["Bar Plot of Counts", "Pandas", *get_source_and_image(7, cells)]
    ]

    env = Environment(loader=FileSystemLoader('web'), extensions=['jinja2_highlight.HighlightExtension'])
    template = env.get_template('t_index.html')
    output_from_parsed_template = template.render(foo=output)


    # to save the results
    with open("web/index.html", "w") as fh:
        fh.write(output_from_parsed_template)
