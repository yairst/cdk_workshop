from constructs import Construct
from aws_cdk import (
    Stack
)

class WorkshopPipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(self, id, **kwargs)

        # Pipeline code will go here