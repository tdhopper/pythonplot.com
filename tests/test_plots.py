import render

defined_plots = {'bar-counts': ['pandas', 'plotnine', 'ggplot'],
                 'dodged-bar-chart': ['pandas', 'plotnine', 'ggplot'],
                 'scatter-plot': ['pandas', 'plotnine', 'ggplot'],
                 'scatter-plot-with-colors': ['matplotlib',
                                              'seaborn',
                                              'plotnine',
                                              'ggplot'],
                 'scatter-plot-with-facet': ['seaborn', 'plotnine', 'ggplot'],
                 'scatter-plot-with-facets': ['seaborn', 'plotnine', 'ggplot'],
                 'scatter-plot-with-size': ['pandas', 'plotnine', 'ggplot'],
                 'scatter-with-regression': ['seaborn', 'plotnine', 'ggplot'],
                 'simple-histogram': ['pandas', 'matplotlib', 'plotnine', 'ggplot', 'bokeh'],
                 'stacked-bar-chart': ['pandas', 'plotnine', 'ggplot'],
                 'stacked-kde': ['pandas', 'seaborn', 'plotnine', 'ggplot'],
                 'stacked-smooth-line-and-scatter': ['plotnine', 'ggplot'],
                 'timeseries': ['pandas', 'plotnine', 'ggplot']}


def test_exist():
    plots = render.extract_cells("Examples.ipynb")
    for name, slug in plots:
        names = [d['package-slug'] for d in plots[(name, slug)]]
        assert set(names) == set(defined_plots[slug])
