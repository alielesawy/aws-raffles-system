import boto3
import os

def create_lambda_function():
    lambda_client = boto3.client('lambda', region_name="us-east-1")  

    # IAM Role ARN
    role_arn = "arn:aws:iam::010526266619:role/lamda-role-raffle"

    # Path to your zipped Lambda function
    zip_file_path = "apply.zip"  # Update with the actual path

    # Read the ZIP file as binary
    with open(zip_file_path, 'rb') as f:
        zip_data = f.read()

    try:
        response = lambda_client.create_function(
            FunctionName='ApplyFunction',
            Runtime='nodejs18.x',
            Role=role_arn,
            Handler='apply.handler', 
            Code={
                'ZipFile': zip_data
            },
            Description='Lambda function created via boto3',
            Timeout=2,
            MemorySize=128,
            Publish=True
        )

        print(f"Lambda function created successfully: {response['FunctionArn']}")

    except Exception as e:
        print(f"Error creating Lambda function: {str(e)}")

if __name__ == '__main__':
    create_lambda_function()
