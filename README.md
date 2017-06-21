
## An Introduction to Python Plotting for Exploratory Data Analysis

Available at [pythonplot.com](http://pythonplot.com/)

### Contributing

The site is generated from plots in the `ggplot vs Python Plotting.ipynb` Python 3, Jupyter notebook.

Each plot is tagged with metadata using Jupyter cell tags. You can view the cell tags in your notebook with `View > Cell Toolbar > Tags`.

The tags look like this:

```
ex
name:scatter-with-regression
package:ggplot
```

`ex` identifies the cell as an example. The `name` tag corresponds to an item in the `names` dictionary in `render.py`. The `package` tag corresponds to a package in the `packages` dict in `render.py`.

At the moment, the code must return a png image into the output cell. A Markdown comment can be added within triple quotes on the first line of the cell. (This currently doesn't work for `R` cells.)

You can render the images to `web/index.html` by running `$ make`.