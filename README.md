<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->

<!-- display the social media buttons in your README -->

By Tim Hopper:
[tdhopper.com](http://www.tdhopper.com)

[![alt text][1.1]][1]
[![alt text][6.1]][6]


<!-- links to social media icons -->
<!-- no need to change these -->

<!-- icons with padding -->

[1.1]: http://i.imgur.com/tXSoThF.png (twitter icon with padding)
[2.1]: http://i.imgur.com/P3YfQoD.png (facebook icon with padding)
[3.1]: http://i.imgur.com/yCsTjba.png (google plus icon with padding)
[4.1]: http://i.imgur.com/YckIOms.png (tumblr icon with padding)
[5.1]: http://i.imgur.com/1AGmwO3.png (dribbble icon with padding)
[6.1]: http://i.imgur.com/0o48UoR.png (github icon with padding)

<!-- icons without padding -->

[1.2]: http://i.imgur.com/wWzX9uB.png (twitter icon without padding)
[2.2]: http://i.imgur.com/fep1WsG.png (facebook icon without padding)
[3.2]: http://i.imgur.com/VlgBKQ9.png (google plus icon without padding)
[4.2]: http://i.imgur.com/jDRp47c.png (tumblr icon without padding)
[5.2]: http://i.imgur.com/Vvy3Kru.png (dribbble icon without padding)
[6.2]: http://i.imgur.com/9I6NRUm.png (github icon without padding)


<!-- links to your social media accounts -->
<!-- update these accordingly -->

[1]: http://www.twitter.com/tdhopper
[6]: http://www.github.com/tdhopper

<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->

[![Build Status](https://travis-ci.org/tdhopper/pythonplot.com.svg?branch=master)](https://travis-ci.org/tdhopper/pythonplot.com)

## An Introduction to Python Plotting for Exploratory Data Analysis

Available at [pythonplot.com](http://pythonplot.com/)

### Contributing

The site is generated from plots in the `Examples.ipynb` Python 3, Jupyter notebook.

You can create a [Conda](https://conda.io/docs/install/quick.html) dev environment to run the notebook with `make dev_environment`.

Each plot in the notebook is tagged with metadata using Jupyter cell tags. You can view the cell tags in your notebook with `View > Cell Toolbar > Tags`.

The tags look like this:

```
ex
name:scatter-with-regression
package:ggplot
```

`ex` identifies the cell as an example. The `name` tag corresponds to an item in the `names` dictionary in `render.py`. The `package` tag corresponds to a package in the `packages` dict in `render.py`.

At the moment, the code must return a png image into the output cell. A Markdown comment can be added within triple quotes on the first line of the cell. (This currently doesn't work for `R` cells.)

You can render the images to `web/index.html` by running `$ make`.