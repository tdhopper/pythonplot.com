import boto3
import time

client = boto3.client('cloudfront')

response = client.create_invalidation(
    DistributionId='EL6HA8RZFI08I',
    InvalidationBatch={
        'Paths': {
            'Quantity': 2,
            'Items': [
                '/index.html',
                '/img/plots/*'
            ]
        },
        'CallerReference': str(time.time())
    }
)
print(response)
