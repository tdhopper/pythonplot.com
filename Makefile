
OUTPUTDIR=web

S3_BUCKET=catskill-sitcom-mew

all: render s3_upload
	echo "Done"

render:
	/Users/tdhopper/miniconda2/envs/ggplot_vs_python_viz/bin/python render.py

s3_upload:
	s3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed --guess-mime-type --no-mime-magic --no-preserve

run_nb:
	jupyter nbconvert --to notebook --execute "ggplot vs Python Plotting.ipynb"

.PHONY: all render s3_upload run_nb
