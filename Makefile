GIT_COMMIT=$(shell git log -1 --pretty=format:"%h")
OUTPUTDIR=web

S3_BUCKET=pythonplot.com

all: render s3_upload

clean:
	rm -f Examples.*.ipynb
	rm -f *.pyc
	rm -f  .Rhistory

travis: test render
	python ./.travis/ authenticate_plotly.py

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

dev_environment:
	conda env update
	source activate pythonplot && pip install -r requirements.txt

cloudfront_invalidate:
	python .travis/invalidate_cloudfront.py

.PHONY: all qrender render s3_upload run_nb travis clean cloudfront_invalidate test dev_environment