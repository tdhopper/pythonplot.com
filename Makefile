GIT_COMMIT=$(shell git log -1 --pretty=format:"%h")
OUTPUTDIR=web

all: render

clean:
	rm -f Examples.*.ipynb
	rm -f *.pyc
	rm -f  .Rhistory
	rm -f .setup_done

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

run_nb: .setup_done
	uv run jupyter nbconvert --to notebook --execute "Examples.ipynb" --output "Examples.$(GIT_COMMIT).ipynb"

dev_environment: setup
	@echo "Development environment ready!"

.PHONY: all qrender render run_nb clean test dev_environment setup
