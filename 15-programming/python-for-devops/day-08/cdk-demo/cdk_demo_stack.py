from aws_cdk import Stack
from aws_cdk import aws_s3 as s3
from constructs import Construct


class CdkDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(self, "DemoBucket", versioned=True)
