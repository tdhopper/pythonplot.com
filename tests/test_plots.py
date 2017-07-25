import render

defined_plots = {'bar-counts': ['pandas', 'plotnine', 'ggplot', 'plotly', ],
                 'dodged-bar-chart': ['pandas', 'plotnine', 'ggplot', 'plotly', ],
                 'scatter-plot': ['pandas', 'plotnine', 'ggplot', 'plotly', ],
                 'scatter-plot-with-colors': ['matplotlib',
                                              'seaborn',
                                              'plotnine',
                                              'ggplot',
                                              'plotly', ],
                 'scatter-plot-with-facet': ['seaborn', 'plotnine', 'ggplot', 'plotly', ],
                 'scatter-plot-with-facets': ['seaborn', 'plotnine', 'ggplot', 'plotly', ],
                 'scatter-plot-with-size': ['pandas', 'plotnine', 'ggplot', 'plotly', ],
                 'scatter-with-regression': ['seaborn', 'plotnine', 'ggplot', 'plotly', ],
                 'simple-histogram': ['pandas', 'matplotlib', 'plotnine', 'ggplot', 'plotly', ],
                 'stacked-bar-chart': ['pandas', 'plotnine', 'ggplot', 'plotly', ],
                 'stacked-kde': ['pandas', 'seaborn', 'plotnine', 'ggplot', 'plotly', ],
                 'stacked-smooth-line-and-scatter': ['plotnine', 'ggplot', 'plotly', ],
                 'timeseries': ['pandas', 'plotnine', 'ggplot', 'plotly', ]}


def test_exist():
    plots = render.extract_cells("Examples.ipynb")
    for name, slug in plots:
        names = [d['package-slug'] for d in plots[(name, slug)]]
        assert set(names) == set(defined_plots[slug])
