GIT_COMMIT=$(shell git log -1 --pretty=format:"%h")
OUTPUTDIR=web

S3_BUCKET=pythonplot.com

all: render s3_upload
	echo "Done"

clean:
	rm -f Examples.*.ipynb
	rm -f *.pyc
	rm -f  .Rhistory

travis: render
	echo "Done"

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

linux_conda:
	wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
	bash miniconda.sh -b -p $HOME/miniconda
	rm -f miniconda.sh
	hash -r
	conda config --set always_yes yes --set changeps1 no
	conda update -q conda
	conda info -a
	conda install r-essentials pip
	conda install -c r rpy2

.PHONY: all render s3_upload run_nb travis clean cloudfront_invalidate linux_conda