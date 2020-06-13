## Introduction
Plotting is an essential component of data analysis. As a data scientist,
I spend a significant amount of my time making simple plots to understand complex data sets (exploratory data analysis) and help others understand them (presentations).

In particular, I make a lot of bar charts (including histograms), line plots (including time series), scatter plots, and density plots from data in [Pandas data frames](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html "pandas.DataFrame documentation"). I often want to facet these on various categorical variables and layer them on a common grid.

### Python Plotting Options

Python plotting libraries are manifold. Most well known is Matplotlib.

"[Matplotlib](https://matplotlib.org/ "Matplotlib: Python plotting") is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms." Native Matplotlib is the cause of [frustration](https://stackoverflow.com/questions/tagged/matplotlib) to many data analysts due to the complex syntax. Much of that frustration would be alleviated if it were recognized as a library of lower level plotting primitives on which other tools can be built. (If you are frustrated by Matplotlib and haven't read [Effectively Using Matplotlib](http://pbpython.com/effective-matplotlib.html) by [Chris Moffitt](https://twitter.com/chris1610), go read it.)

#### Matplotlib-Based Libraries

Many excellent plotting tools are built on top of Matplotlib.

[Pandas plots](https://pandas.pydata.org/pandas-docs/stable/visualization.html "pandas documentation") provides the "basics to easily create decent looking plots" from data frames. It provides about 70% of what I want to do day-to-day. Importantly, it lacks robust faceting capabilities.

"[plotnine](https://plotnine.readthedocs.io/en/stable/) is an implementation of a grammar of graphics in Python, it is based on ggplot2." plotnine is a attempt to directly translate ggplot2 to Python; despite some quirks and bugs, it works very well for a young product.

"[Seaborn](https://seaborn.pydata.org/ "Seaborn: statistical data visualization") is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics." Seaborn makes beautiful plots but is geared toward specific statistical plots, not general purpose plotting. It does have a powerful [faceting utility function](http://seaborn.pydata.org/tutorial/axis_grids.html) that I use regularly.

#### Interactive Plotting Libraries

There are several tools that can make the kinds of plots described here. At present, I have little experience with them. If anyone would like to help add examples, please [get in touch](https://github.com/tdhopper/pythonplot.com).

"[Altair](https://altair-viz.github.io/ "Declarative Visualization in Python") is a declarative statistical visualization library for Python, based on [Vega-Lite](https://vega.github.io/vega-lite/ "Vega-Lite: A High-Level Visualization Grammar for Interactive Graphics")." According to [Jake Vanderplas](https://speakerdeck.com/jakevdp/visualization-in-python-with-altair), "Declarative visualization lets you think about data and relationships, rather than incidental details." I provide Altair examples rendered as static images.


"[plotly](https://plot.ly/ "Plotly - Make charts and dashboards online")'s Python graphing library makes interactive, publication-quality graphs online. Examples of how to make line plots, scatter plots, area charts, bar charts, error bars, box plots, histograms, heatmaps, subplots, multiple-axes, polar charts, and bubble charts." I provide plotly examples rendered as static images.

"[Bokeh](http://bokeh.pydata.org/en/latest/ "Python interactive visualization library") is a Python interactive visualization library that targets modern web browsers for presentation."

"[bqplot](https://github.com/bloomberg/bqplot) is a Grammar of Graphics-based interactive plotting framework for the Jupyter notebook."

### The Python Plotting Landscape

If you're interested in the breadth of plotting tools available for Python, I commend Jake Vanderplas's Pycon 2017 talk called the [The Python Visualization Landscape](https://www.youtube.com/watch?v=FytuB8nFHPQ). Similarly, the blogpost [A Dramatic Tour through Python's Data Visualization Landscape (including ggplot and Altair)](https://dsaber.com/2016/10/02/a-dramatic-tour-through-pythons-data-visualization-landscape-including-ggplot-and-altair/) by Dan Saber is worth your time.

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
