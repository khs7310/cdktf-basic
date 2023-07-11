#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.provider import Instance
from cdktf_cdktf_provider_aws.provider import VPC

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

    def create_vpc(self, id: str, cidr_block: str):
        return Vpc(self.stack, id, provider=self.provider, cidr_block=cidr_block)

    def create_eks_cluster(self, id: str, vpc_id: str, cluster_version: str):
        return EksCluster(self.stack, id, provider=self.provider, vpc_config=[{"subnetIds": ["subnet-12345678"], "vpcId": vpc_id}], version=cluster_version)

    def create_eks_node_group(self, id: str, eks_cluster_id: str, instance_types: list, desired_capacity: int):
        return EksNodeGroup(self.stack, id, provider=self.provider, cluster_name=eks_cluster_id, instance_types=instance_types, desired_capacity=desired_capacity)



class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here
        
        provider = AwsProvider(self, "AWS", region="ap-northeast-2")
        resource_factory = ResourceFactory(self, provider)

        vpc = resource_factory.create_vpc("my-vpc", "10.0.0.0/16")

        eks_cluster = resource_factory.create_eks_cluster("my-eks-cluster", vpc.vpc_id, "1.20")

        eks_node_group = resource_factory.create_eks_node_group("my-eks-node-group", eks_cluster.cluster_name, ["t3.medium"], 3)

        helm_release = resource_factory.create_helm_release("my-helm-release", "nginx-stable/nginx-ingress", "default")


        





app = App()
MyStack(app, "ec2-depth-1")

app.synth()
