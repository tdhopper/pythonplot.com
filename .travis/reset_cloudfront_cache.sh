###############################################################################
###  Resets CloudFront cache with boto/cfadmin utility
###  Run: ./this_script  
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

#
# Install boto
#
echo -e "\nInstalling boto...\n"
git clone git://github.com/boto/boto.git
cd boto
sudo python setup.py install
cd ../
rm -rf boto

#
# Set up credentials for boto
#
echo -e "\nSet up boto credentials...\n"
cat > ~/.boto < 
# XNXNXXNNNNXNXN - distribution configured for the Web - in aws amazon cloudfront distributions.
#
echo -e "\nCloudFront Invalidating...\n"
cfadmin invalidate XNXNXXNNNNXNXN /yoursite.com
cfadmin invalidate XNXNXXNNNNXNXN /.yoursite.com
cfadmin invalidate XNXNXXNNNNXNXN /index.html /static/main.css /static/main.js
echo -e "\nInvalidating is in progress...\n"
echo -e "\nYou can check the status on the 'Invalidations' tab here https://console.aws.amazon.com/cloudfront/home?region=your_region#distribution-settings:XNXNXXNNNNXNXN\n"

#
# Clean up
#
echo -e "\nRemove boto config file\n"
rm ~/.boto
