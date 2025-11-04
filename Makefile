GIT_COMMIT=$(shell git log -1 --pretty=format:"%h")
OUTPUTDIR=web

S3_BUCKET=pythonplot.com

all: render s3_upload

clean:
	rm -f Examples.*.ipynb
	rm -f *.pyc
	rm -f  .Rhistory

travis: render

setup:
	@echo "Setting up development environment..."
	@echo "1. Installing Python dependencies with uv..."
	@command -v uv >/dev/null 2>&1 || { echo "Installing uv..."; curl -LsSf https://astral.sh/uv/install.sh | sh; }
	uv pip install -r requirements.txt
	@echo "2. Installing R packages..."
	@./setup_r.sh
	@echo "✓ Setup complete!"

test:
	python -m pytest tests/

qrender:
	python render.py "Examples.ipynb"

render: run_nb
	python render.py "Examples.$(GIT_COMMIT).ipynb"

s3_upload:
	s3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed --guess-mime-type --no-mime-magic --no-preserve

run_nb:
	jupyter nbconvert --to notebook --execute "Examples.ipynb" --output "Examples.$(GIT_COMMIT).ipynb"

dev_environment: setup
	@echo "Development environment ready!"
	@echo ""
	@echo "Note: This project now uses uv instead of conda."
	@echo "R must be installed separately on your system."

cloudfront_invalidate:
	python .travis/invalidate_cloudfront.py

.PHONY: all qrender render s3_upload run_nb travis clean cloudfront_invalidate test dev_environment setup
