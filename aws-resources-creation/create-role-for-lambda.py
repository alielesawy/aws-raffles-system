
import boto3
import json

iam = boto3.client('iam')

# Define the trust policy for Lambda
trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

# Create the IAM role
try:
    role = iam.create_role(
        RoleName='lamda-role-raffle',
        AssumeRolePolicyDocument=json.dumps(trust_policy)
    )

    # Attach required policies
    policy_arns = [
        'arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess',
        'arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole',
        'arn:aws:iam::aws:policy/CloudWatchLogsFullAccess'
    ]

    for policy_arn in policy_arns:
        iam.attach_role_policy(
            RoleName='lamda-role-raffle',
            PolicyArn=policy_arn
        )

    print(f"Role 'lamda-role-raffle' created successfully with required policies")

except iam.exceptions.EntityAlreadyExistsException:
    print(f"Role 'lamda-role-raffle' already exists")
except Exception as e:
    print(f"Error creating role: {str(e)}")