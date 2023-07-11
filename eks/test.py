from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_aws.provider import AwsProvider


from cdktf_cdktf_provider_aws.vpc import Vpc
from cdktf_cdktf_provider_aws.eks_cluster import EksCluster
from cdktf_cdktf_provider_aws.eks_node_group import EksNodeGroup
# from cdktf_cdktf_provider_kubernetes.helm_release import HelmRelease


class ResourceFactory:
    def __init__(self, stack: TerraformStack, provider: AwsProvider):
        self.stack = stack
        self.provider = provider

    def create_resource(self, strAWSResource, strResourceName, objecct_data):
        
        object  =  strAWSResource ( strResourceName, **object_data)
        return object



class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here
        
        provider = AwsProvider(self, "AWS", region="ap-northeast-2")
        
        resource_factory = ResourceFactory(self, provider)

        vpc = resource_factory.create_vpc("Vpc", "my-vpc", "10.0.0.0/16")