# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

pythonplot.com is a static website that provides a visual comparison of different Python plotting libraries (pandas, matplotlib, seaborn, plotnine, plotly, altair) and R's ggplot2 for exploratory data analysis. It serves as a "Rosetta Stone" showing how to create the same plots across different libraries.

## Architecture

The site is generated from a Jupyter notebook (Examples.ipynb) that contains tagged code cells. The build process:

1. Executes the notebook using `jupyter nbconvert`
2. Extracts tagged cells using `render.py`
3. Generates static HTML using Jinja2 templates
4. Outputs PNG images and an HTML file to the `web/` directory

### Key Components

- **Examples.ipynb**: Source notebook containing plot examples for each library
- **render.py**: Core build script that:
  - Extracts cells tagged with metadata (ex, name:*, package:*)
  - Extracts base64 PNG images from cell outputs and saves them to web/img/plots/
  - Parses cell source code and optional markdown comments
  - Renders the final HTML using Jinja2
- **templates/t_index.html**: Jinja2 template for the website
- **web/**: Output directory for generated site
- **INTRO.md**: Markdown content for the site introduction

### Cell Tagging System

Notebook cells must be tagged with metadata for the render script to process them:

```
ex                        # Marks cell as an example
name:scatter-plot         # Maps to names dict in render.py
package:seaborn           # Maps to packages dict in render.py
```

Valid plot names and packages are defined in dictionaries at the top of render.py (lines 19-43).

## Development Commands

### Setup Environment

```bash
make dev_environment    # Installs Python and R dependencies using uv
make setup             # Alternative command (same as dev_environment)
```

**Prerequisites:**
- Python 3.11+ installed on system
- R 4.0+ installed separately (via Homebrew, apt, or CRAN)
- uv package manager (auto-installed by make targets if missing)

**Manual Setup:**
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Python dependencies
uv pip install -r requirements.txt

# Install R packages (ggplot2, mgcv)
./setup_r.sh
```

### Build Site

```bash
make qrender           # Quick render from Examples.ipynb without executing
make render            # Full build: execute notebook, then render (creates timestamped .ipynb)
make                   # Full build + S3 upload
```

The render process:
1. `make render` runs the notebook with `jupyter nbconvert --execute`
2. Creates a git-commit-stamped copy (Examples.<hash>.ipynb)
3. Runs `python render.py` to extract cells and generate web/index.html
4. PNG images are extracted and saved to web/img/plots/ with MD5-based filenames

### Testing

```bash
make test              # Run pytest tests
python -m pytest tests/
```

The test suite (tests/test_plots.py) validates that Examples.ipynb contains all expected plot/package combinations defined in the defined_plots dictionary.

### Local Development

After rendering, serve locally:

```bash
cd web && python -m http.server
```

### Image Rendering

All plots are rendered to static PNG images:
- **Plotly**: Uses Kaleido for local rendering (no authentication required with v5+)
- **Altair**: Uses native rendering or selenium/geckodriver
- **R/ggplot2**: Uses rpy2 to interface with system R installation

**Note**: Plotly authentication is no longer needed with plotly v5+. The old authentication code in `.travis/authenticate_plotly.py` is deprecated.

## Adding New Plots

1. Add the plot name to the `names` dictionary in render.py
2. Add a new cell in Examples.ipynb with code that produces a PNG output
3. Tag the cell with: `ex`, `name:<plot-name>`, `package:<library-name>`
4. Keep code lines under ~46 characters to avoid horizontal scrolling in the UI
5. Optionally add a markdown comment in triple quotes on the first line
6. Update tests/test_plots.py to include the new plot in defined_plots
7. Run `make qrender` to test (or `make render` for full rebuild)

## Technical Constraints

- Plot code must generate PNG output in the notebook cell
- For plotly, images must be generated via their server (requires credentials)
- R code cells must start with `%%R` magic command
- Altair cells must start with `%%altair` magic command
- Code lines should wrap to ~46 characters for proper display
- All image paths are MD5 hashes of the base64-encoded PNG data

## Dependencies

### Python Environment
- **Python**: 3.11+ (specified in runtime.txt and pyproject.toml)
- **Package Manager**: uv (modern, fast alternative to pip)
- **Jupyter**: For notebook execution

### Plotting Libraries (all latest versions)
- pandas 2.0+
- matplotlib 3.7+
- seaborn 0.13+
- plotnine 0.13+
- plotly 5.24+ (with Kaleido for image export)
- altair 5.0+
- statsmodels 0.14+

### R Environment
- **R**: 4.0+ (system installation required)
- **R Packages**: ggplot2, mgcv
- **Python-R Bridge**: rpy2 3.5+

### Other Key Dependencies
- Jinja2 with jinja2-highlight for templating
- selenium 4.15+ with geckodriver for browser automation
- markdown for text processing

**Configuration Files:**
- `pyproject.toml`: Modern Python project metadata and dependencies
- `requirements.txt`: Pin-free dependency list
- `setup_r.sh`: R package installation script

## CI/CD

The project uses **GitHub Actions** for continuous integration and deployment (migrated from Travis CI).

### Workflow (.github/workflows/deploy.yml)

**On Every Push:**
1. Setup R 4.3 using r-lib/setup-r action
2. Install R packages (ggplot2, mgcv)
3. Setup Python 3.11
4. Install uv and Python dependencies
5. Setup Firefox and geckodriver for selenium
6. Run pytest tests with xvfb (virtual display)
7. Execute notebook and render site
8. Deploy to Netlify:
   - **master branch**: Production deployment
   - **Other branches**: Preview deployments

**Required Secrets:**
- `NETLIFY_AUTH_TOKEN`: Netlify authentication token
- `NETLIFY_SITE_ID`: Netlify site identifier

**Environment Variables:**
- `R_HOME`: Set to R installation path (e.g., `/opt/R/4.3.3/lib/R` on GitHub runners)

### Legacy CI Files
- `.travis.yml`: Old Travis CI config (deprecated)
- `.travis/`: Old CI scripts (mostly deprecated)
- `.travis/authenticate_plotly.py`: No longer needed with plotly v5+
