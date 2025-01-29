import boto3

def create_api_gateway():
    client = boto3.client('apigateway')

    # Step 1: Create REST API
    api = client.create_rest_api(
        name='RaffleAPI',
        description='My HTTP API Gateway',
        endpointConfiguration={'types': ['REGIONAL']}
    )
    api_id = api['id']
    
    print(f"Created API Gateway with ID: {api_id}")

    # Step 2: Get Root Resource ID
    resources = client.get_resources(restApiId=api_id)
    root_resource_id = resources['items'][0]['id']
    
    # Step 3: Create a new resource (e.g., `/raffle`)
    resource = client.create_resource(
        restApiId=api_id,
        parentId=root_resource_id,
        pathPart='raffle'
    )
    resource_id = resource['id']
    
    print(f"Created resource /raffle with ID: {resource_id}")

    # Step 4: Create a GET method on `/raffle`
    client.put_method(
        restApiId=api_id,
        resourceId=resource_id,
        httpMethod='GET',
        authorizationType='NONE'
    )
    
    print("Created GET method on /raffle")

    # Step 5: Create a mock integration (for testing)
    client.put_integration(
        restApiId=api_id,
        resourceId=resource_id,
        httpMethod='GET',
        type='MOCK'
    )

    # Step 6: Deploy the API
    deployment = client.create_deployment(
        restApiId=api_id,
        stageName='dev',
        description='Initial deployment'
    )
    deployment_id = deployment['id']
    
    print(f"Created deployment with ID: {deployment_id}")

    return api_id

if __name__ == "__main__":
    create_api_gateway()
