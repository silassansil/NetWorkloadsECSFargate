from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
)
from constructs import Construct


class InfraStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        dynamodb.Table(
            self,
            "Weather",
            partition_key=dynamodb.Attribute(
                name="Location", type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="Timestamp", type=dynamodb.AttributeType.STRING
            ),
        )
