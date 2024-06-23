import boto3
from botocore.exceptions import ClientError
import os
print(os.environ.get('ACCESS_KEY_ID'))
print(os.environ.get('SECRET_ACCESS_KEY'))
# Environment variables
access_key_id = os.environ.get('ACCESS_KEY_ID')
secret_access_key = os.environ.get('SECRET_ACCESS_KEY')
endpoint_url = 'https://5868f1c65dbb2a8c20cd09e90d5d3c29.r2.cloudflarestorage.com'
bucket_name = 'my-facegram-storage'

s3 = boto3.client(
    's3',
    endpoint_url=endpoint_url,
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key
)

try:
    s3.upload_file('testfile.txt', bucket_name, 'testfile.txt')
    print("Upload Successful")
except ClientError as e:
    print(f"Upload failed: {e}")
