#!/bin/bash

# Setup script for R and required R packages
# This script installs the R packages needed for pythonplot.com

set -e  # Exit on error

echo "Installing R packages..."

# Check if R is installed
if ! command -v R &> /dev/null; then
    echo "Error: R is not installed."
    echo ""
    echo "Please install R first:"
    echo "  - macOS: brew install r"
    echo "  - Ubuntu/Debian: sudo apt-get install r-base r-base-dev"
    echo "  - Or download from: https://cran.r-project.org/"
    exit 1
fi

echo "R version:"
R --version | head -n 1

# Install required R packages
R --quiet --no-save << 'EOF'
# Set CRAN mirror
options(repos = c(CRAN = "https://cran.rstudio.com/"))

# List of required packages
packages <- c("ggplot2", "mgcv")

# Install packages that aren't already installed
for (pkg in packages) {
    if (!require(pkg, character.only = TRUE, quietly = TRUE)) {
        cat(paste("Installing", pkg, "...\n"))
        install.packages(pkg, quiet = FALSE)
    } else {
        cat(paste(pkg, "is already installed\n"))
    }
}

# Verify installations
cat("\nVerifying R package installations:\n")
for (pkg in packages) {
    if (require(pkg, character.only = TRUE, quietly = TRUE)) {
        cat(paste("✓", pkg, "version", as.character(packageVersion(pkg)), "\n"))
    } else {
        cat(paste("✗", pkg, "FAILED TO INSTALL\n"))
        quit(status = 1)
    }
}

cat("\n✓ All R packages installed successfully!\n")
EOF

echo ""
echo "R setup complete!"
echo ""
echo "Note: If you encounter issues with rpy2, make sure R_HOME is set correctly:"
echo "  export R_HOME=\$(R RHOME)"
