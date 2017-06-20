# Python Plotting for Exploratory Analysis

> "The simple graph has brought more information to the data analyst's
mind than any other device." — John Tukey

Plotting is an essential component of data analysis. As a data scientist,
I spend a significant amount of my time making simple plots to understand complex data sets (exploratory data analysis) and help others understand them (presentations).

##### ggplot2, a consistent interface with sane defaults

Before I started using Python, I did most of my data analysis work in [R](https://cran.r-project.org/ "The Comprehensive R Archive Network"). I remain a big fan of Hadley Wickham's [ggplot2](http://ggplot2.org/ "ggplot2"), a "[grammar of graphics](https://www.amazon.com/Grammar-Graphics-Statistics-Computing/dp/0387245448 "The Grammar of Graphics (Statistics and Computing): Leland Wilkinson, D. Wills, D. Rope, A. Norton, R. Dubbs: 9780387245447: Amazon.com: Books")" implementation in R, for exploratory data analysis.

Like [scikit-learn](http://scikit-learn.org/ "scikit-learn: machine learning in Python") for machine learning in Python, ggplot2 provides a consistent API with sane defaults. The consistent interface makes it easier to iterate rapidly with low cognitive overhead. The sane defaults makes it easy to drop plots right into an email or presentation.

Particularly, ggplot2 allows the user to make basic plots (bar, histogram, line, scatter, density, violin) from data frames _with_ [faceting](http://ggplot2.tidyverse.org/reference/facet_grid.html) and [layering](https://rpubs.com/hadley/ggplot2-layers) by discrete values.

An excellent introduction to the power of ggplot2 is in Hadley Wickham and Garrett Grolemund's book [R for Data Science](http://r4ds.had.co.nz/data-visualisation.html).

##### The Python Plotting Landscape

In the past 5 years, I've been a heavy Python user and haven't found a comparable tool that lets me complete these tasks with the ease of ggplot2.
Of course, Python plotting libraries are manifold. Here are some of the well known libraries (with descriptions taken from their webpages):

* [Matplotlib](https://matplotlib.org/ "Matplotlib: Python plotting"): "Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms."
* [seaborn](https://seaborn.pydata.org/ "Seaborn: statistical data visualization"): "Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics."
* [Pandas plots](https://pandas.pydata.org/pandas-docs/stable/visualization.html "pandas documentation"): "basics to easily create decent looking plots" from data frames using on Matplotlib under the hood.
* [ggpy](https://github.com/yhat/ggpy "ggplot port for python"): A "ggplot port for Python" that isn't under active development.
* [plotnine](https://plotnine.readthedocs.io/en/stable/ "plotnine: A grammar of graphics for Python"): "plotnine is an implementation of a grammar of graphics in Python, it is based on ggplot2."
* [Altair](https://altair-viz.github.io/ "Declarative Visualization in Python"): "Altair is a declarative statistical visualization library for Python, based on Vega-Lite."
* [Bokeh](http://bokeh.pydata.org/en/latest/ "Python interactive visualization library"): "Bokeh is a Python interactive visualization library that targets modern web browsers for presentation."

__Matplotlib__ is powerful, but it doesn't provide high-level syntax for rapid iteration. __Seaborn__ makes beautiful plots but is geared toward specific statistical plots, not general purpose plotting; however, it does have a powerful faceting utility function that I use regularly. Pandas plots are wonderful and easy, but they are not easily faceted and often require lower-level matplotlib tweaks.

__ggpy__ appears to be abandoned. __plotnine__ is a recent attempt to directly translate ggplot2 to Python; despite some quirks and bugs, it works very well for a young product. Also new on the scene, __Altair__ offers a lot of promise, but I haven't used it much yet. It will have significant changes in the 2.0 release. I won't focus on __Bokeh__ here since I'm more interested in static (non-interactive) plots for now.

If you're interested in the breadth of plotting tools available for Python, I commend Jake Vanderplas's Pycon 2017 talk called the [The Python Visualization Landscape](https://www.youtube.com/watch?v=FytuB8nFHPQ). Similarly, the blogpost [A Dramatic Tour through Python’s Data Visualization Landscape (including ggplot and Altair)](https://dsaber.com/2016/10/02/a-dramatic-tour-through-pythons-data-visualization-landscape-including-ggplot-and-altair/) by Dan Saber is worth your time.

##### Humble Rosetta Stone for Visualization in Exploratory Data Analysis

After years of complaining on Twitter, I have started compiling my thoughts on what we are lacking in Python. Below I have begun compiling a list of basic plots for exploratory data analysis. I have generated the plots with as many different libraries as time (and library) permits.

My hope is that this will (1) help you in your daily practice to work with what is available and (2) help inspire future development of Python plotting libraries.

[Feedback](https://github.com/tdhopper/ggplot_vs_python_vis/issues) or other  plot suggestions are welcome.

##### Hearty Thank You

Much Python plotting development is done by open source developers who have an (almost) thankless task. I am extremely grateful for the countless hours of many who have helped me do my job. Please keep it up!