import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the S3 client
s3 = boto3.client('s3')

try:
    # List all buckets to test credentials
    response = s3.list_buckets()
    print("Buckets available:", [bucket['Name'] for bucket in response['Buckets']])

    # Replace with your bucket name and object key to test access
    bucket_name = "mywavbucket"
    object_key = "Recording(36)_fixed.wav"

    # Generate a pre-signed URL to test object access
    pre_signed_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_key},
        ExpiresIn=3600  # URL valid for 1 hour
    )
    print("Pre-signed URL:", pre_signed_url)

except NoCredentialsError:
    print("Error: AWS credentials not found.")
except PartialCredentialsError:
    print("Error: Incomplete AWS credentials.")
except Exception as e:
    print(f"Error: {str(e)}")
