#!/usr/bin/env python3
from boto.cloudfront import CloudFrontConnection

aws_cf_distribution_id = 'EL6HA8RZFI08I'

objects = ['/index.html']
conn = CloudFrontConnection()
print(conn.create_invalidation_request(aws_cf_distribution_id, objects))
