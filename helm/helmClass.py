#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack

import json
import yaml

#from cdktf_cdktf_provider_helm import HelmRelease
#from cdktf_cdktf_provider_helm.data_helm_template import DataHelmTemplate
from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release



class ResourceFactory:
    def __init__(self, stack: TerraformStack, provider: HelmProvider):
        self.stack = stack
        self.provider = provider

    def create_resource(self, aws_resource, resource_name, **resource_data):
        resource = aws_resource(self.stack, resource_name, provider=self.provider, **resource_data)
        return resource




class helmClass(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here
        #HelmRelease(self, 'helm', )
        #HelmProvider( self,"Helm", kubernetes.config_path="~/.kube/config" )
        config_data = {            
            
            "kubernetes" : {"config_path": "~/.kube/config"}
        }       
        
        provider = HelmProvider( self,"Helm", **config_data )
        self.resource_factory = ResourceFactory(self, provider)
        
        
        
    def deploy(self, helm_name, helm_values_data ):
        #Release(self, helm_name, **helm_values_data)
        #print("helm_value:", helm_values_data)
        #return
        self.resource_factory.create_resource(Release, helm_name, **helm_values_data)
        

app = App()
helm = helmClass(app,"helm" )

with open('values3.yaml', 'r') as f:
    docs = list( yaml.load_all(f, Loader=yaml.FullLoader) )
        
    values_list  = yaml.dump(docs[0])
    print(values_list)  
            

    release_config_data = {
        "chart": "nginx",
        "name": "cdktf-nginx",
        "create_namespace" : True,
        "namespace" : "cdktf-nginx",
        "repository" : "https://charts.bitnami.com/bitnami",
        "version": "15.0.2",
        "values" : [values_list] #data_list
        
    }

#print("release_config", release_config_data)
      

# helm.deploy( "nginx-releases", **release_config_data )
# app.synth()

        
#         values_list2 = '''
# replicaCount: 2
# service:
#     type: LoadBalancer
#     port: 8080
#         '''
        
#         with open('values3.yaml', 'r') as f:
#             docs = list( yaml.load_all(f, Loader=yaml.FullLoader) )
        
#         values_list  = yaml.dump(docs[0])
#         print(values_list)
            
      


#         release_config_data = {
#             "chart": "nginx",
#             "name": "cdktf-nginx",
#             "create_namespace" : True,
#             "namespace" : "cdktf-nginx",
#             "repository" : "https://charts.bitnami.com/bitnami",
#             "version": "15.0.2",
#             # "values": [ 'replicaCount': 3 ]  xx
#             # "values": [ { 'replicaCount': 3 }]    TypeError: type of argument values must be one of (Sequence[str], NoneType); got list instead
#             #"values" : "replicaCount: 2"
#             #"values" : "replicaCount:2"
#             # "values" : output <== json 안됨
#             #instance = "['cpu': '1500m', 'memory': '1500Mi']"
#             #"values"  : "{" + configuration +"}"
#             #----  아래는 됨 ----
#             # "values" : ["replicaCount: 2",
#             #             "fullnameOverride: 'my-cdktf' " ]
#             # "values" : value_three
            
#             #"values" : instance
#             #"values" : [value_next]   #data_list
#             "values" : [values_list] #data_list
            
#         }



#         Release(self, "nginx-releases", **release_config_data)
        
       
        
        


# app = App()
# MyStack(app, "helm")

# app.synth()


#  release_config_data = {
#             "chart": "nginx",
#             "name": "cdktf-nginx",
#             "create_namespace" : True,
#             "namespace" : "cdktf-ngixn",
#             "repository"    : "https://charts.bitnami.com/bitnami",
            
#             #reset_values   true/false
#             # #reuse_values
#            # "values" : ""
            
            
#         }


# + resource "helm_release" "nginx-releases" {
#             + atomic                     = false
#             + chart                      = "nginx"
#             + cleanup_on_fail            = false
#             + create_namespace           = true
#             + dependency_update          = false
#             + disable_crd_hooks          = false
#             + disable_openapi_validation = false
#             + disable_webhooks           = false
#             + force_update               = false
#             + id                         = (known after apply)
#             + lint                       = false
#             + manifest                   = (known after apply)
#             + max_history                = 0
#             + metadata                   = (known after apply)
#             + name                       = "cdktf-nginx"
#             + namespace                  = "cdktf-ngixn"
#             + pass_credentials           = false
#             + recreate_pods              = false
#             + render_subchart_notes      = true
#             + replace                    = false
#             + repository                 = "https://charts.bitnami.com/bitnami"
#             + reset_values               = false
#             + reuse_values               = false
#             + skip_crds                  = false
#             + status                     = "deployed"
#             + timeout                    = 300
#             + verify                     = false
#             + version                    = (known after apply)
#             + wait                       = true
#             + wait_for_jobs              = false
#           }

#       Plan: 1 to add, 0 to change, 0 to destroy.





 # release_config_data = {
        #     "chart": "nginx",
        #     "name": "cdktf-nginx",
        #     "create_namespace" : True,
        #     "namespace" : "cdktf-ngixn",
        #     "repository"    : "https://charts.bitnami.com/bitnami",
        #     "version": "15.0.2",
        #    # "values" : my_data
        #     "values" : {
        #                 'replicaCount': 3,
                            
        #                 }
        #     # reset_values   true/false
        #     # reuse_values
        #     # recreate_pods  true/false
        #    # "values" : ""
            
            
        # }
        
        # Release( self, "nginx-releases",**release_config_data)
        
        
        

    # def __init__(
    #     self,
    #     scope: _constructs_77d1e7e8.Construct,
    #     id_: builtins.str,
    #     *,
    #     chart: builtins.str,
    #     name: builtins.str,
    #     atomic: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     cleanup_on_fail: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     create_namespace: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     dependency_update: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     description: typing.Optional[builtins.str] = None,
    #     devel: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     disable_crd_hooks: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     disable_openapi_validation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     disable_webhooks: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     force_update: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     id: typing.Optional[builtins.str] = None,
    #     keyring: typing.Optional[builtins.str] = None,
    #     lint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     max_history: typing.Optional[jsii.Number] = None,
    #     namespace: typing.Optional[builtins.str] = None,
    #     pass_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     postrender: typing.Optional[typing.Union["ReleasePostrender", typing.Dict[builtins.str, typing.Any]]] = None,
    #     recreate_pods: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     render_subchart_notes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     replace: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     repository: typing.Optional[builtins.str] = None,
    #     repository_ca_file: typing.Optional[builtins.str] = None,
    #     repository_cert_file: typing.Optional[builtins.str] = None,
    #     repository_key_file: typing.Optional[builtins.str] = None,
    #     repository_password: typing.Optional[builtins.str] = None,
    #     repository_username: typing.Optional[builtins.str] = None,
    #     reset_values: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     reuse_values: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     set: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ReleaseSet", typing.Dict[builtins.str, typing.Any]]]]] = None,
    #     set_list: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ReleaseSetListStruct", typing.Dict[builtins.str, typing.Any]]]]] = None,
    #     set_sensitive: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ReleaseSetSensitive", typing.Dict[builtins.str, typing.Any]]]]] = None,
    #     skip_crds: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     timeout: typing.Optional[jsii.Number] = None,
    #     values: typing.Optional[typing.Sequence[builtins.str]] = None,
    #     verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     version: typing.Optional[builtins.str] = None,
    #     wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     wait_for_jobs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    #     connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    #     count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    #     depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    #     for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    #     lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    #     provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    #     provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,        
        