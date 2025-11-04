# Testing Checklist for Modernized Build

This checklist should be completed after setting up the modernized development environment.

## Environment Setup Testing

- [ ] **Install R** (if not already installed)
  ```bash
  # macOS
  brew install r

  # Ubuntu/Debian
  sudo apt-get install r-base r-base-dev
  ```

- [ ] **Run R setup script**
  ```bash
  ./setup_r.sh
  ```
  Expected: ggplot2 and mgcv packages installed successfully

- [ ] **Install Python dependencies with uv**
  ```bash
  # Install uv if needed
  curl -LsSf https://astral.sh/uv/install.sh | sh

  # Install dependencies
  uv pip install -r requirements.txt
  ```
  Expected: All packages install without errors

- [ ] **Verify R integration**
  ```bash
  python -c "import rpy2.robjects as ro; ro.r('library(ggplot2)'); print('R integration works!')"
  ```
  Expected: No errors, prints "R integration works!"

## Build Testing

- [ ] **Run tests**
  ```bash
  make test
  ```
  Expected: All tests pass

- [ ] **Quick render test (without notebook execution)**
  ```bash
  make qrender
  ```
  Expected: Generates web/index.html from existing Examples.ipynb

- [ ] **Full build test (with notebook execution)**
  ```bash
  make render
  ```
  Expected:
  - Executes notebook successfully
  - Generates all plot images in web/img/plots/
  - Creates web/index.html
  - No errors from any plotting library

## Known Migration Issues to Watch For

### Plotly v5 Changes
- [ ] Verify plotly plots render without authentication
- [ ] Check that Kaleido is used for static image export (not Orca)
- [ ] Ensure all plotly examples in notebook still work

### Altair v5 Changes
- [ ] Verify altair plots render to PNG
- [ ] Confirm altair-saver is not needed (using native rendering)
- [ ] Check selenium/geckodriver works for image export

### plotnine 0.13+ Changes
- [ ] Verify all ggplot-style plots render correctly
- [ ] Check for any deprecation warnings

### statsmodels 0.14+ Changes
- [ ] Verify regression line plots work
- [ ] Check confidence interval calculations

### rpy2 3.5+ Changes
- [ ] Verify %%R magic commands work
- [ ] Check data passing between Python and R
- [ ] Ensure all R ggplot2 examples render

### Selenium 4+ Changes
- [ ] Verify geckodriver compatibility
- [ ] Check headless browser operations
- [ ] Test with xvfb if on Linux

## CI/CD Testing

- [ ] **GitHub Actions workflow**
  - Push to a test branch
  - Verify all workflow steps complete
  - Check Netlify preview deploy works
  - Merge to master and verify production deploy

## Performance Checks

- [ ] Note build time for comparison (old vs new)
- [ ] Check generated image file sizes
- [ ] Verify web/index.html loads correctly in browser

## Rollback Plan

If critical issues are found:
1. Keep Travis CI config (.travis.yml) until GitHub Actions is confirmed working
2. Document any notebook cells that fail with new library versions
3. Consider pinning problematic packages to older versions temporarily
