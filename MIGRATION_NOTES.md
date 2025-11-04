# Migration Notes: Modernization to 2025

This document summarizes the modernization work completed on pythonplot.com.

## Overview

The project has been modernized from 2020-era dependencies and infrastructure to 2025 standards:
- Python 3.6 → 3.11
- Conda → uv package manager
- Travis CI → GitHub Actions
- Outdated plotting libraries → Latest versions
- Deprecated packages removed

## Changes Made

### 1. Python Environment Modernization

**New Files:**
- `pyproject.toml`: Modern Python project configuration with all dependencies
- `setup_r.sh`: Script to install R packages (ggplot2, mgcv)

**Updated Files:**
- `runtime.txt`: 3.6 → 3.11
- `requirements.txt`: All packages updated to latest versions with minimum version constraints

**Removed Dependencies:**
- `altair-saver` → Deprecated, using native altair rendering
- `chart-studio` → Not needed with plotly v5 local rendering
- `plotly-orca` → Replaced by Kaleido
- Duplicate `selenium` entry removed

**Updated Dependencies:**
| Package | Old Version | New Version | Notes |
|---------|-------------|-------------|-------|
| plotly | 4.10.0 | 5.24+ | No authentication needed for local rendering |
| plotnine | <0.7.0 | 0.13+ | Better ggplot2 compatibility |
| statsmodels | 0.11.1 | 0.14+ | Security fixes |
| seaborn | (latest) | 0.13+ | Updated API |
| altair | (latest) | 5.0+ | Major version bump |
| rpy2 | (unversioned) | 3.5+ | Python 3.11+ compatible |
| selenium | (duplicated) | 4.15+ | API changes in v4 |
| pandas | (latest) | 2.0+ | Major improvements |
| matplotlib | (latest) | 3.7+ | Modern features |

### 2. R Integration Updates

**Approach:** Separate system R installation (no longer using conda)

**Changes:**
- Created `setup_r.sh` to install R packages
- R must be installed separately (via Homebrew, apt, or CRAN)
- rpy2 updated to work with system R and Python 3.11+
- Documentation updated to explain R setup

**Environment Variable:** `R_HOME` must be set correctly for rpy2 to work

### 3. Build System Updates

**Makefile Changes:**
- Removed `plotly_auth` target (no longer needed)
- Added `setup` target for uv-based dependency installation
- Updated `dev_environment` to use uv instead of conda
- Updated `.PHONY` declarations

**What Didn't Change:**
- Core build targets (`render`, `qrender`, `test`, `run_nb`)
- render.py script (compatible with new libraries)
- Notebook structure and tagging system

### 4. CI/CD Migration

**From:** Travis CI
**To:** GitHub Actions

**New File:** `.github/workflows/deploy.yml`

**Workflow Features:**
- Uses r-lib/setup-r for R installation
- Uses uv for Python dependencies
- Runs on every push and pull request
- Automatic Netlify deployment:
  - Production: master branch
  - Preview: all other branches

**Required GitHub Secrets:**
- `NETLIFY_AUTH_TOKEN`
- `NETLIFY_SITE_ID`

**Legacy Files (Now Deprecated):**
- `.travis.yml`
- `.travis/authenticate_plotly.py` (marked deprecated with explanation)
- `.travis/install_conda.sh` (wasn't being used)
- `.travis/invalidate_cloudfront.py` (not needed with Netlify)

### 5. Documentation Updates

**README.md:**
- Added modern development setup instructions
- Updated to reflect uv usage
- Added build and CI/CD sections
- Clarified plotly no longer needs authentication

**CLAUDE.md:**
- Updated all dependency versions
- Documented new setup process
- Added CI/CD section
- Updated technical constraints

**New Documentation:**
- `TESTING_CHECKLIST.md`: Comprehensive testing guide for first build
- `MIGRATION_NOTES.md`: This file

## Next Steps

### Before First Build

1. **Install System Dependencies:**
   ```bash
   # macOS
   brew install r

   # Ubuntu/Debian
   sudo apt-get install r-base r-base-dev
   ```

2. **Set Up Development Environment:**
   ```bash
   make dev_environment
   ```

3. **Verify Setup:**
   ```bash
   # Test Python packages
   python -c "import pandas, plotly, seaborn, plotnine, altair, rpy2; print('✓ Python packages OK')"

   # Test R integration
   python -c "import rpy2.robjects as ro; ro.r('library(ggplot2)'); print('✓ R integration OK')"
   ```

### Testing the Build

4. **Run Tests:**
   ```bash
   make test
   ```

5. **Try Quick Render (no notebook execution):**
   ```bash
   make qrender
   ```

6. **Full Build (executes notebook):**
   ```bash
   make render
   ```
   - This will take several minutes
   - Watch for any library compatibility issues
   - Check `TESTING_CHECKLIST.md` for specific things to verify

### Setting Up CI/CD

7. **Configure GitHub Secrets:**
   - Go to your GitHub repo → Settings → Secrets and variables → Actions
   - Add `NETLIFY_AUTH_TOKEN` (from Netlify account settings)
   - Add `NETLIFY_SITE_ID` (from Netlify site settings)

8. **Test GitHub Actions:**
   - Push to a test branch
   - Check Actions tab to see workflow run
   - Verify Netlify preview deployment

9. **Deploy to Production:**
   - Merge to master branch
   - GitHub Actions will automatically deploy to production

## Potential Issues to Watch For

### Library Compatibility

1. **plotly v5 Changes:**
   - API changes from v4 to v5
   - Different image rendering (Kaleido vs Orca)
   - No authentication needed

2. **altair v5 Changes:**
   - May need updates to save PNG images
   - Selenium/geckodriver integration

3. **plotnine 0.13:**
   - Better ggplot2 compatibility but some API changes

4. **statsmodels 0.14:**
   - Check regression plots and confidence intervals

### Environment Issues

1. **R_HOME:**
   - Must be set correctly for rpy2
   - GitHub Actions sets this automatically
   - Locally: `export R_HOME=$(R RHOME)`

2. **Headless Rendering:**
   - Selenium needs xvfb on Linux
   - GitHub Actions handles this automatically
   - Locally on Linux: `xvfb-run make render`

3. **geckodriver:**
   - Must be in PATH for selenium
   - GitHub Actions installs this automatically
   - Locally: Install via package manager or download

## Rollback Plan

If you encounter critical issues:

1. **Keep Travis CI temporarily:**
   - Don't delete `.travis.yml` until GitHub Actions is proven
   - Both can run simultaneously

2. **Pin problematic packages:**
   - If specific library versions cause issues, pin to older versions in requirements.txt
   - Example: `plotly==4.14.3` if v5 has problems

3. **Gradual migration:**
   - Update libraries one at a time
   - Test each change thoroughly

## Files Changed Summary

**New Files:**
- `pyproject.toml`
- `setup_r.sh`
- `.github/workflows/deploy.yml`
- `TESTING_CHECKLIST.md`
- `MIGRATION_NOTES.md`

**Modified Files:**
- `runtime.txt`
- `requirements.txt`
- `Makefile`
- `README.md`
- `CLAUDE.md`
- `.travis/authenticate_plotly.py` (deprecated with explanation)

**Deprecated (Not Deleted):**
- `environment.yml` (conda environment - no longer used)
- `.travis.yml` (Travis CI config)
- `.travis/` directory (old CI scripts)

**No Changes:**
- `render.py` (compatible with new libraries)
- `Examples.ipynb` (may need updates if libraries break examples)
- `templates/t_index.html`
- `tests/test_plots.py`
- `INTRO.md`

## Success Criteria

The migration is successful when:

- [ ] `make dev_environment` completes without errors
- [ ] `make test` passes all tests
- [ ] `make render` executes notebook and generates all plots
- [ ] GitHub Actions workflow runs successfully
- [ ] Site deploys correctly to Netlify
- [ ] All plotting libraries render correctly
- [ ] R ggplot2 examples work via rpy2

## Support

If you encounter issues:

1. Check `TESTING_CHECKLIST.md` for common problems
2. Review GitHub Actions logs for CI issues
3. Check package compatibility in individual notebook cells
4. File issues in the GitHub repository

---

**Migration completed:** 2025-11-04
**Python version:** 3.11+
**Primary changes:** uv adoption, library updates, CI/CD modernization
