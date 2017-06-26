###############################################################################
###  Resets CloudFront cache with boto/cfadmin utility
###  Run: ./reset_cloudfront_cache.sh
###############################################################################

#
# Travis specific part - run this script only for production
#

# If this is fork - just exit
if [[ -n "${TRAVIS_PULL_REQUEST}" && "${TRAVIS_PULL_REQUEST}" != "false"  ]]; then
  echo -e '\n============== deploy will not be started (from the fork) ==============\n'
  exit 0
fi

if [[ $TRAVIS_BRANCH == 'master' ]]; then
    echo -e "\nThis is master/production branch - let's reset the CloudFront cache\n"
else
    echo -e "\nReset of CloudFront cache will not be started for non-production branch - exit.\n"
    exit 0
fi

echo -e "\nCloudFront Invalidating...\n"
cfadmin invalidate XNXNXXNNNNXNXN /yoursite.com
cfadmin invalidate XNXNXXNNNNXNXN /.yoursite.com
cfadmin invalidate XNXNXXNNNNXNXN /index.html /static/main.css /static/main.js
echo -e "\nInvalidating is in progress...\n"
echo -e "\nYou can check the status on the 'Invalidations' tab here https://console.aws.amazon.com/cloudfront/home?region=your_region#distribution-settings:XNXNXXNNNNXNXN\n"
