#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput

from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance


import json


class FactoryConstruct(TerraformStack) : 
    
    InstancesObject = []
    Instances = []
    instance =None
    
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope,id)
        self.provider = AwsProvider( self, "AWS", region="ap-northeast-2")
        
        for i in range(2):
            self.instance = Instance(self, "compute" + str(i),
                            ami="ami-0e05f79e46019bfac",
                            instance_type="t2.micro",
                            )
            self.Instances.append(self.instance)

        #print("instance: ", self.Instances)
        json_instances = []
        
        
        outPut = None
        for i in range(2):
            outPut = TerraformOutput(self, "public_ip2" +str(i),
                        value=self.Instances[i].public_ip,
                        )
            
        print("output", outPut)
        
        # self.instance = Instance(self, "compute",
        #                     ami="ami-01456a894f71116f2",
        #                     instance_type="t2.micro",
        #                     )
        # self.instance2 = Instance(self, "compute2",
        #                     ami="ami-01456a894f71116f2",
        #                     instance_type="t2.micro",
        #                     )
        


# class MyStack(TerraformStack):
#     def __init__(self, scope: Construct, id: str):
#         super().__init__(scope, id)

#         # define resources here
#         AwsProvider(self, "AWS", region="ap-northeast-2")
#         instance = Instance(self, "compute",
#                             ami="ami-01456a894f71116f2",
#                             instance_type="t2.micro",
#                             )

#         # TerraformOutput(self, "public_ip",
#         #                 value=instance.public_ip,
#         #                 )


app = App()
#MyStack(app, "ec2-instance")
FactoryConstruct(app, "ec2-instance-factory")
app.synth()
