
OUTPUTDIR=web

S3_BUCKET=catskill-sitcom-mew

publish:
	cd

s3_upload: publish
	s3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed --guess-mime-type --no-mime-magic --no-preserve

.PHONY: publish s3_upload
