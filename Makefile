GIT_COMMIT=$(shell git log -1 --pretty=format:"%h")
OUTPUTDIR=web

S3_BUCKET=pythonplot.com

all: render

deploy: render s3_upload

clean:
	rm -f Examples.*.ipynb
	rm -f *.pyc
	rm -f  .Rhistory
	rm -f .setup_done

travis: render

.setup_done:
	@echo "Setting up development environment..."
	@echo "1. Installing Python dependencies with uv..."
	@command -v uv >/dev/null 2>&1 || { echo "Installing uv..."; curl -LsSf https://astral.sh/uv/install.sh | sh; }
	uv sync
	@echo "2. Installing Chrome for Kaleido..."
	@uv run kaleido_get_chrome || echo "Chrome may already be installed"
	@echo "3. Installing R packages..."
	@./setup_r.sh
	@echo "✓ Setup complete!"
	@touch .setup_done

setup: .setup_done

test: .setup_done
	uv run pytest tests/

qrender: .setup_done
	uv run python render.py "Examples.ipynb"

render: .setup_done run_nb
	uv run python render.py "Examples.$(GIT_COMMIT).ipynb"

s3_upload:
	s3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed --guess-mime-type --no-mime-magic --no-preserve

run_nb: .setup_done
	uv run jupyter nbconvert --to notebook --execute "Examples.ipynb" --output "Examples.$(GIT_COMMIT).ipynb"

dev_environment: setup
	@echo "Development environment ready!"
	@echo ""
	@echo "Note: This project now uses uv instead of conda."
	@echo "R must be installed separately on your system."

cloudfront_invalidate:
	python .travis/invalidate_cloudfront.py

.PHONY: all deploy qrender render s3_upload run_nb travis clean cloudfront_invalidate test dev_environment setup
