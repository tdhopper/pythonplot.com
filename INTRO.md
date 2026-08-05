## Introduction
Plotting is an essential component of data analysis. As a data scientist,
I spend a significant amount of my time making simple plots to understand complex data sets (exploratory data analysis) and help others understand them (presentations).

In particular, I make a lot of bar charts (including histograms), line plots (including time series), scatter plots, and density plots from data in [Pandas data frames](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html "pandas.DataFrame documentation"). I often want to facet these on various categorical variables and layer them on a common grid.

### Python Plotting Options

Python has many plotting libraries. Matplotlib is the best known, and several others build on it.

"[Matplotlib](https://matplotlib.org/ "Matplotlib: Visualization with Python") makes easy things easy and hard things possible." It hands you figures, axes, and drawing primitives. You assemble everything above that level yourself: faceting, stacking, density estimation, smoothing. That assembly is what sends analysts to [Stack Overflow](https://stackoverflow.com/questions/tagged/matplotlib).

Put the Matplotlib and ggplot2 versions of the two-variable faceted scatter plot below side by side: eighteen lines of subplot bookkeeping against four lines of grammar. If Matplotlib annoys you and you haven't read [Effectively Using Matplotlib](http://pbpython.com/effective-matplotlib.html) by [Chris Moffitt](https://twitter.com/chris1610), go read it.

#### Matplotlib-Based Libraries

[Pandas plotting](https://pandas.pydata.org/docs/user_guide/visualization.html "pandas user guide: Chart Visualization") provides "the basics ... to easily create decent looking plots" from data frames. That is about 70% of what I do day-to-day. It has no faceting, no categorical color mapping, and no smoothing, so five of the examples below have no pandas column.

Seaborn calls itself "[statistical data visualization](https://seaborn.pydata.org/ "seaborn: statistical data visualization")." Its classic interface is a set of named functions (`histplot`, `scatterplot`, `countplot`, `lmplot`, `kdeplot`) plus [FacetGrid](http://seaborn.pydata.org/tutorial/axis_grids.html), which I use for faceting more than anything else in the library. It covers every plot below, once you know which function to reach for.

Seaborn 0.12 added [seaborn.objects](https://seaborn.pydata.org/tutorial/objects_interface.html), a second interface built on the grammar of graphics. It composes a plot from marks and statistical transforms instead of dispatching to a named plotting function. The interface has no loess smoother and no regression confidence band, so those two examples are missing.

"[plotnine](https://plotnine.org/) is a data visualization package for Python based on the grammar of graphics." It tracks ggplot2 closely enough that most R code translates line for line, down to the `+` for layering. I reach for it when I want ggplot2 semantics without leaving Python.

#### Interactive Plotting Libraries

These libraries draw in the browser. The examples here are static PNGs, so their tooltips, panning, and linked selection are gone.

"[Vega-Altair](https://altair-viz.github.io/ "Vega-Altair: Declarative Visualization in Python") is a declarative visualization library for Python," built on [Vega-Lite](https://vega.github.io/vega-lite/ "Vega-Lite: A High-Level Visualization Grammar for Interactive Graphics"). According to [Jake Vanderplas](https://speakerdeck.com/jakevdp/visualization-in-python-with-altair), "Declarative visualization lets you think about data and relationships, rather than incidental details." You describe the encoding and Altair chooses the marks, scales, and legend.

"[plotly](https://plotly.com/python/ "Plotly Open Source Graphing Library for Python")'s Python graphing library makes interactive, publication-quality graphs." The examples here use [Plotly Express](https://plotly.com/python/plotly-express/), which the project calls "the recommended starting point for creating most common figures." Express covers most of these plots in one call; the regression and smoothing examples fall back to `graph_objects` and statsmodels.

JetBrains writes [Lets-Plot](https://lets-plot.org/ "Lets-Plot: multiplatform plotting library built on the principles of the Grammar of Graphics"), which it calls "a faithful port of R's ggplot2 to Python and Kotlin." The claim holds up: most of the examples below are the ggplot2 column with `lp.` prefixes. Like Altair, it renders to HTML in the notebook.

"[Bokeh](https://docs.bokeh.org/en/latest/ "Bokeh documentation") is a Python library for creating interactive visualizations for modern web browsers." The Bokeh examples below go through [hvPlot](https://hvplot.holoviz.org/), which adds an `.hvplot` accessor to data frames. The accessor echoes the pandas `.plot` API, so most of these plots are one call plus a few keyword arguments. hvPlot has no regression line or loess smoother, so it is absent from those two examples.

### Further Reading

Jake Vanderplas's PyCon 2017 talk [The Python Visualization Landscape](https://www.youtube.com/watch?v=FytuB8nFHPQ) still explains how these libraries relate to one another, as does Dan Saber's [A Dramatic Tour through Python's Data Visualization Landscape (including ggplot and Altair)](https://dsaber.com/2016/10/02/a-dramatic-tour-through-pythons-data-visualization-landscape-including-ggplot-and-altair/). Both predate several of the libraries here, but the family tree they draw holds.

### Hearty Thank You

Much Python plotting development is done by open source developers who have an (almost) thankless task. I am extremely grateful for the countless hours of many who have helped me do my job. Please keep it up!

### Why all the talk about ggplot?

The word "ggplot" comes up a lot in discussions of plotting. Before I started using Python, I did most of my data analysis work in [R](https://cran.r-project.org/ "The Comprehensive R Archive Network"). I, with many Pythonistas, remain a big fan of Hadley Wickham's [ggplot2](http://ggplot2.org/ "ggplot2"), a "[grammar of graphics](https://www.amazon.com/Grammar-Graphics-Statistics-Computing/dp/0387245448 "The Grammar of Graphics (Statistics and Computing): Leland Wilkinson, D. Wills, D. Rope, A. Norton, R. Dubbs: 9780387245447: Amazon.com: Books")" implementation in R, for exploratory data analysis.

Like [scikit-learn](http://scikit-learn.org/ "scikit-learn: machine learning in Python") for machine learning in Python, ggplot2 provides a consistent API with sane defaults. The consistent interface makes it easier to iterate rapidly with low cognitive overhead. The sane defaults makes it easy to drop plots right into an email or presentation.

Particularly, ggplot2 allows the user to make basic plots (bar, histogram, line, scatter, density, violin) from data frames _with_ [faceting](http://ggplot2.tidyverse.org/reference/facet_grid.html) and [layering](https://rpubs.com/hadley/ggplot2-layers) by discrete values.

An excellent introduction to the power of ggplot2 is in Hadley Wickham and Garrett Grolemund's book [R for Data Science](http://r4ds.had.co.nz/data-visualisation.html).

### Humble Rosetta Stone for Visualization in Exploratory Data Analysis

Below I have begun compiling a list of basic plots for exploratory data analysis. I have generated the plots with as many different libraries as time (and library) permits.

My hope is that this will (1) help you in your daily practice to work with what is available and (2) help inspire future development of Python plotting libraries.

Some rudimentary instructions on how you can contribute plots are [here](https://github.com/tdhopper/pythonplot.com#contributing). [General feedback or other plot suggestions](https://github.com/tdhopper/pythonplot.com/issues) are welcome.

#### Data

The datasets used below are included with ggplot2. One is the [Prices of 50,000 round cut diamonds](http://ggplot2.tidyverse.org/reference/diamonds.html) and the other is [Fuel economy data from 1999 and 2008 for 38 popular models of car](http://ggplot2.tidyverse.org/reference/mpg.html).

The time series example is a random walk I generate with a quick Python script.

Here's what a few rows of the datasets looks like:
