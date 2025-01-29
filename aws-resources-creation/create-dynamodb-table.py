import boto3

# Create DynamoDB client with region
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Create table
response = dynamodb.create_table(
    TableName='RaffleUsers',  
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S' ,
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'
        }
    ],
    BillingMode='PAY_PER_REQUEST',
    TableClass='STANDARD_INFREQUENT_ACCESS'
)

print("Table created successfully:", response)
