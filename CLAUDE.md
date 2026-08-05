# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

pythonplot.com is a static website that provides a visual comparison of different Python plotting libraries (pandas, matplotlib, seaborn, plotnine, lets-plot, plotly, altair) and R's ggplot2 for exploratory data analysis. It serves as a "Rosetta Stone" showing how to create the same plots across different libraries.

## Architecture

The site is generated from a Jupyter notebook (Examples.ipynb) that contains tagged code cells. The build process:

1. Executes the notebook using `jupyter nbconvert`
2. Extracts tagged cells using `render.py`
3. Generates static HTML using Jinja2 templates
4. Outputs PNG images and an HTML file to the `web/` directory

The checked-in Examples.ipynb has no outputs; the site can only be rendered from an executed copy of the notebook.

### Key Components

- **Examples.ipynb**: Source notebook containing plot examples for each library
- **render.py**: Core build script that:
  - Extracts cells tagged with metadata (ex, name:*, package:*)
  - Extracts base64 PNG images from cell outputs and saves them to web/img/plots/
  - Parses cell source code and optional markdown comments
  - Renders the final HTML using Jinja2
- **templates/t_index.html**: Jinja2 template for the website
- **web/**: Output directory for generated site; web/css/ (checked in) holds custom.css and pygments-native.css
- **INTRO.md**: Markdown content for the site introduction

### Cell Tagging System

Notebook cells must be tagged with metadata for the render script to process them:

```
ex                        # Marks cell as an example
name:scatter-plot         # Maps to names dict in render.py
package:seaborn           # Maps to packages dict in render.py
```

Valid plot names and packages are defined in dictionaries at the top of render.py.

## Development Commands

### Setup Environment

```bash
make setup    # uv sync, Chrome for Kaleido, R packages
```

**Prerequisites:**
- R 4.0+ installed separately (via Homebrew, apt, or CRAN)
- uv package manager (auto-installed by make targets if missing; uv provides Python)

**Manual Setup:**
```bash
uv sync         # Python dependencies (pyproject.toml + uv.lock)
uv run kaleido_get_chrome   # Chrome for plotly PNG export
./setup_r.sh    # R packages (ggplot2, mgcv)
```

### Build Site

```bash
make qrender   # Render from an already-executed Examples.ipynb (fails if outputs are stripped)
make render    # Full build: execute notebook, then render (creates git-hash-stamped .ipynb)
```

The render process:
1. `make render` runs the notebook with `jupyter nbconvert --execute`
2. Creates a git-commit-stamped copy (Examples.<hash>.ipynb)
3. Runs `python render.py` to extract cells and generate web/index.html
4. PNG images are extracted and saved to web/img/plots/ with MD5-based filenames

### Testing

```bash
make test              # Run pytest tests
```

The test suite (tests/test_plots.py) validates that Examples.ipynb contains all expected plot/package tag combinations. It reads tags only, so it works on the outputs-stripped notebook.

### Local Development

After rendering, serve locally:

```bash
cd web && python -m http.server
```

### Image Rendering

All plots are rendered to static PNG images inside the executed notebook:
- **Plotly**: `pio.renderers.default = "png"` with Kaleido (needs Chrome; `uv run kaleido_get_chrome`)
- **Altair**: `alt.renderers.enable("png")` with vl-convert-python (set in the notebook's first cell — do not remove)
- **R/ggplot2**: rpy2 against the system R installation (`%%R` cell magic)
- **Lets-Plot** and **hvPlot/Bokeh**: an `image/png` IPython formatter registered in the notebook's first cell. Bokeh has no headless renderer, so hvPlot figures are screenshotted through Selenium driving the same Chrome for Testing build Kaleido downloads; Selenium Manager fetches the matching chromedriver on first use (needs network).

## Adding New Plots

1. Add the plot name to the `names` dictionary in render.py
2. Add a new cell in Examples.ipynb with code that produces a PNG output
3. Tag the cell with: `ex`, `name:<plot-name>`, `package:<library-name>`
4. Keep code lines under ~46 characters to avoid horizontal scrolling in the UI
5. Optionally add a markdown comment in triple quotes on the first line
6. Update tests/test_plots.py to include the new plot in defined_plots
7. Run `make render` and inspect web/index.html

## Technical Constraints

- Plot code must generate PNG output in the notebook cell
- R code cells must start with `%%R` magic command
- Code lines should wrap to ~46 characters for proper display
- All image paths are MD5 hashes of the base64-encoded PNG data

## Dependencies

Python dependencies are declared in `pyproject.toml` and locked in `uv.lock` (committed). Key libraries: pandas, matplotlib, seaborn, plotnine, lets-plot, plotly (+kaleido), altair (+vl-convert-python), statsmodels, rpy2, Jinja2 with jinja2-highlight.

R (system install) with ggplot2 and mgcv, installed by `setup_r.sh`.

## CI/CD

GitHub Actions (`.github/workflows/deploy.yml`) on every push:

1. Setup R (r-lib/actions, RSPM binary packages) and install ggplot2/mgcv
2. Install uv (astral-sh/setup-uv with caching) and `uv sync`
3. `uv run kaleido_get_chrome`
4. Run pytest
5. Execute notebook and render site
6. Deploy `web/` to Cloudflare Pages (project `pythonplot`, direct upload via `cloudflare/wrangler-action`)

Master pushes deploy with `--branch=main`, which the Cloudflare project treats as its
production branch (pythonplot.com, www.pythonplot.com). Every other branch deploys with
its own branch name, producing a preview URL.

**Required Secrets:** `CLOUDFLARE_API_TOKEN` (needs the Cloudflare Pages: Edit
permission), `CLOUDFLARE_ACCOUNT_ID`
