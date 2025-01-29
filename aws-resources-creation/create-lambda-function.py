
import aws_cdk as cdk
from aws_cdk import aws_lambda as lambda_

class LambdaStack(cdk.Stack):
    def __init__(self, scope: cdk.App, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create Lambda function
        lambda_function = lambda_.Function(
            self, 
            "MyLambdaFunction",
            runtime=lambda_.Runtime.NODEJS_20_X,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda"),
            role='lamda-role-raffle' # Assumes role was created previously
        )