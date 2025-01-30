
import boto3
import os

def create_s3_bucket_and_upload_cert():
    # Initialize S3 client
    s3_client = boto3.client('s3')
    bucket_name = 's3bucket-for-apigateway'

    try:
        # Create S3 bucket
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Successfully created bucket {bucket_name}")

        # Specify the local path to your certificate files
        cert_path = input("C/Program Files/Amazon/RootCA.pem")

        # Check if file exists
        if os.path.exists(cert_path):
            # Extract filename from path
            file_name = os.path.basename(cert_path)
            
            # Upload file to S3
            s3_client.upload_file(cert_path, bucket_name, file_name)
            print(f"Successfully uploaded {file_name} to {bucket_name}")
        else:
            print("Certificate file not found at specified path")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    create_s3_bucket_and_upload_cert()