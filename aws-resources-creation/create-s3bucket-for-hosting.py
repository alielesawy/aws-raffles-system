
import boto3
import json

# Initialize S3 client
s3_client = boto3.client('s3')
bucket_name = 'XXXXXXXXXXXXXXXXXX'

# Create bucket
try:
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"Created bucket: {bucket_name}")
except Exception as e:
    print(f"Error creating bucket: {e}")

# Create bucket policy for website hosting
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket_name}/*"
        }
    ]
}

# Apply bucket policy
try:
    s3_client.put_bucket_policy(
        Bucket=bucket_name,
        Policy=json.dumps(bucket_policy)
    )
    print("Applied bucket policy for website hosting")
except Exception as e:
    print(f"Error applying bucket policy: {e}")

# Enable website hosting
website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Key': 'index.html'}
}

try:
    s3_client.put_bucket_website(
        Bucket=bucket_name,
        WebsiteConfiguration=website_configuration
    )
    print("Enabled website hosting")
except Exception as e:
    print(f"Error enabling website hosting: {e}")

# Upload HTML files
html_files = ['apply.html', 'draw.html']

for file_name in html_files:
    try:
        s3_client.upload_file(
            file_name, 
            bucket_name, 
            f'website/{file_name}',
            ExtraArgs={'ContentType': 'text/html'}
        )
        print(f"Uploaded {file_name}")
    except Exception as e:
        print(f"Error uploading {file_name}: {e}")

print(f"Website URL: http://{bucket_name}.s3-website-{s3_client.meta.region_name}.amazonaws.com")