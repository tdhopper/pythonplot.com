#!/bin/bash

if [ $TRAVIS_BRANCH = "foo" ]; then
    netlify deploy \
        --auth $NETLIFY_AUTH_TOKEN \
        --site $NETLIFY_SITE_ID \
        --dir ./web \
        --prod \
        --message "Production deploy from Travis CI"
else 
    netlify deploy \
        --auth $NETLIFY_AUTH_TOKEN \
        --site $NETLIFY_SITE_ID \
        --dir ./web \
        --message "Preview deploy from Travis CI" \
        --prod
fi
