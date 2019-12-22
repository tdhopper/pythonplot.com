import render

defined_plots = {
    "bar-counts": ["pandas", "plotnine", "ggplot", "plotly", "altair",],
    "dodged-bar-chart": ["pandas", "plotnine", "ggplot", "plotly", "altair",],
    "scatter-plot": ["pandas", "plotnine", "ggplot", "plotly", "altair",],
    "scatter-plot-with-colors": [
        "matplotlib",
        "seaborn",
        "plotnine",
        "ggplot",
        "plotly",
        "altair",
    ],
    "scatter-plot-with-facet": [
        "seaborn",
        "plotnine",
        "ggplot",
        "plotly",
        "altair",
    ],
    "scatter-plot-with-facets": [
        "seaborn",
        "plotnine",
        "ggplot",
        "plotly",
        "altair",
    ],
    "scatter-plot-with-size": [
        "pandas",
        "plotnine",
        "ggplot",
        "plotly",
        "altair",
    ],
    "scatter-with-regression": ["seaborn", "plotnine", "ggplot", "plotly",],
    "simple-histogram": [
        "pandas",
        "matplotlib",
        "plotnine",
        "ggplot",
        "plotly",
        "altair",
    ],
    "stacked-bar-chart": ["pandas", "plotnine", "ggplot", "plotly", "altair",],
    "stacked-kde": [
        "pandas",
        "seaborn",
        "plotnine",
        "ggplot",
        "plotly",
        "altair",
    ],
    "stacked-smooth-line-and-scatter": [
        "plotnine",
        "ggplot",
        "plotly",
        "altair",
    ],
    "timeseries": ["pandas", "plotnine", "ggplot", "plotly", "altair",],
}


def test_exist():
    plots = render.extract_cells("Examples.ipynb")
    for name, slug in plots:
        names = [d["package-slug"] for d in plots[(name, slug)]]
        assert set(names) == set(defined_plots[slug])
