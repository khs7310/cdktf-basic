#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack

import json
import yaml

#from cdktf_cdktf_provider_helm import HelmRelease
#from cdktf_cdktf_provider_helm.data_helm_template import DataHelmTemplate
from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here
        #HelmRelease(self, 'helm', )
        #HelmProvider( self,"Helm", kubernetes.config_path="~/.kube/config" )
        config_data = {            
            
            "kubernetes" : {"config_path": "~/.kube/config"}
        }       
        
        HelmProvider( self,"Helm",**config_data )
        
        
        
        values_list2 = '''
replicaCount: 2
service:
    type: LoadBalancer
    port: 8080
        '''
        
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
            # "values": [ 'replicaCount': 3 ]  xx
            # "values": [ { 'replicaCount': 3 }]    TypeError: type of argument values must be one of (Sequence[str], NoneType); got list instead
            #"values" : "replicaCount: 2"
            #"values" : "replicaCount:2"
            # "values" : output <== json 안됨
            #instance = "['cpu': '1500m', 'memory': '1500Mi']"
            #"values"  : "{" + configuration +"}"
            #----  아래는 됨 ----
            # "values" : ["replicaCount: 2",
            #             "fullnameOverride: 'my-cdktf' " ]
            # "values" : value_three
            
            #"values" : instance
            #"values" : [value_next]   #data_list
            "values" : [values_list] #data_list
            
        }



        Release(self, "nginx-releases", **release_config_data)
        
       
        
        


app = App()
MyStack(app, "helm")

app.synth()


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
        
        