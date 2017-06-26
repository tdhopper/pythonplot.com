import boto3

client = boto3.client('cloudfront')

response = client.create_invalidation(
    DistributionId='EL6HA8RZFI08I',
    InvalidationBatch={
        'Paths': {
            'Quantity': 1,
            'Items': [
                '/index.html',
            ]
        },
        'CallerReference': 'string'
    }
)
print(response)
