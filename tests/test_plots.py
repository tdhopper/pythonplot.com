import json
from collections import defaultdict

defined_plots = {
    "bar-counts": [
        "pandas", "seaborn-objects", "plotnine", "lets-plot", "ggplot", "plotly", "altair",
    ],
    "dodged-bar-chart": [
        "pandas", "seaborn-objects", "plotnine", "lets-plot", "ggplot", "plotly", "altair",
    ],
    "scatter-plot": [
        "pandas", "seaborn-objects", "plotnine", "lets-plot", "ggplot", "plotly", "altair",
    ],
    "scatter-plot-with-colors": [
        "matplotlib",
        "seaborn",
        "seaborn-objects",
        "plotnine",
        "lets-plot",
        "ggplot",
        "plotly",
        "altair",
    ],
    "scatter-plot-with-facet": [
        "seaborn", "seaborn-objects", "plotnine", "lets-plot", "ggplot", "plotly", "altair",
    ],
    "scatter-plot-with-facets": [
        "seaborn", "seaborn-objects", "plotnine", "lets-plot", "ggplot", "plotly", "altair",
    ],
    "scatter-plot-with-size": [
        "pandas", "seaborn-objects", "plotnine", "lets-plot", "ggplot", "plotly", "altair",
    ],
    "scatter-with-regression": [
        "seaborn", "plotnine", "lets-plot", "ggplot", "plotly",
    ],
    "simple-histogram": [
        "pandas",
        "matplotlib",
        "seaborn-objects",
        "plotnine",
        "lets-plot",
        "ggplot",
        "plotly",
        "altair",
    ],
    "stacked-bar-chart": [
        "pandas", "seaborn-objects", "plotnine", "lets-plot", "ggplot", "plotly", "altair",
    ],
    "stacked-kde": [
        "pandas",
        "seaborn",
        "seaborn-objects",
        "plotnine",
        "lets-plot",
        "ggplot",
        "plotly",
        "altair",
    ],
    "stacked-smooth-line-and-scatter": [
        "plotnine", "lets-plot", "ggplot", "plotly", "altair",
    ],
    "timeseries": [
        "pandas", "seaborn-objects", "plotnine", "lets-plot", "ggplot", "plotly", "altair",
    ],
}


def test_exist():
    with open("Examples.ipynb") as f:
        nb = json.load(f)

    found = defaultdict(set)
    for cell in nb["cells"]:
        tags = set(cell["metadata"].get("tags") or [])
        if "ex" not in tags:
            continue
        parsed = {t.split(":")[0]: t.split(":")[1] for t in tags if ":" in t}
        found[parsed["name"]].add(parsed["package"])

    assert {k: set(v) for k, v in defined_plots.items()} == dict(found)
