#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
#from cdktf_cdktf_provider_helm.data_helm_template import DataHelmTemplate
from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release



import yaml

from time import sleep
from multiprocessing import Process, Queue
from ShellCommand import ShellCommandDB
import shlex 
import subprocess





CDK_DEPLOY = 1
CDK_DEPLOY_AUTOAPPROVE = 2






class ResourceFactory_T():
    helmProvider = None
    providerId = "helmProvider"
    app = None
    
    def __init__(self,  provider_config ):            
        self.app = App()
        self.Terraform = TerraformStack(self.app, "helm_terraform")  # <== tfstat name : terraform_변수명
        #self.Terraform = TerraformStack(App(), "helm_terraform")  # <== tfstat name : terraform_변수명
        
        
        
        self.provider_config = provider_config        
        self.helmProvider = HelmProvider( scope = self.Terraform ,id = "helm_provider_id" ,  **self.provider_config ) 
        
    #     "resources": [
    # {
    #   "mode": "managed",
    #   "type": "helm_release",
    #   "name": "helm_provider_id_name_helm_EDD37856",      name : provider_id + helm_resource_name
    # #   "provider": "provider[\"registry.terraform.io/hashicorp/helm\"]",
        
        

    def create_resource(self, helm_name,  **resource_data):
        
        
        resource_helm = Release( scope=self.helmProvider,  id_= helm_name, **resource_data)
    #     "resources": [
        # {
        #   "mode": "managed",
        #   "type": "helm_release",
        #   "name": "helm_nginx51_B9732471",  <== self.resourceID
        sleep(1)
        self.app.synth()
        #resource_helm = {}
        return resource_helm




class helmClass(): 
    
    
    # resoucre factories class 변수
    resource_factory = None   
    init_helm_provider = False
    resource_helm_data = None
    resource_helm_name = ""
    
   
    def __init__(self):
        
        self.kube_config_data = {            
            "kubernetes" : {"config_path": "~/.kube/config"}
        }       
        
        if self.init_helm_provider == False:
            self.resource_factory = ResourceFactory_T( self.kube_config_data)
            self.init_helm_provider = True
        
    def helm_Input_data(self, resource_helm_name:str,  **resource_data):  
        self.resource_helm_name = resource_helm_name
        self.resource_helm_data = resource_data
        
        
        self.resource_factory.create_resource(self.resource_helm_name, **self.resource_helm_data)
            
    def helm_Input_data2(self, resource_helm_name:str, pathFileName  , **resource_data):  
        self.resource_helm_name = resource_helm_name
        self.resource_helm_data = resource_data
        if pathFileName != "" and pathFileName != None :  # and pathFileName != null
            if len(pathFileName) >= 5:
                self.openFileValues( pathFileName)
            
            
        print("self.resource_helm_data: ", self.resource_helm_data)
        
        self.resource_factory.create_resource(self.resource_helm_name, **self.resource_helm_data)
        
        
    def deploy(self,depoy_auto_applove=False ):     
        
        
        if depoy_auto_applove == False : 
            shell = ShellCommandDB( 100,1000, 'cdktf diff') 
            sCapture = shell.Excute_Capture_All_Value()
            
        else: 
            shell = ShellCommandDB( 100,1000, 'cdktf deploy --auto-approve') 
            sCapture = shell.Excute_Capture_All_Value()
            
            
        print("out:=====> ", sCapture.stdout)
        print("err:=====>", sCapture.stderr)
        print("returncode:=====>", sCapture.returncode)
            
        return sCapture
    
    # def destroy(self,depoy_auto_applove=False ):                              
        
    #     if depoy_auto_applove == False : 
    #         shell = ShellCommandDB( 100,1000, 'cdktf diff') 
    #         sCapture = shell.Excute_Capture_All_Value()
            
    #     else: 
    #         shell = ShellCommandDB( 100,1000, 'cdktf destroy --auto-approve') 
    #         sCapture = shell.Excute_Capture_All_Value()
            
            
    #     print("out:=====> ", sCapture.stdout)
    #     print("err:=====>", sCapture.stderr)
    #     print("returncode:=====>", sCapture.returncode)
            
    #     return sCapture
    
    def openFileValues(self, pathFileName):
        with open(pathFileName, 'r') as f:
            docs = list( yaml.load_all(f, Loader=yaml.FullLoader) )
        
        values_list  = yaml.dump(docs[0])
        self.setHelmInfoValue( values_list )
        return values_list
        #print(values_list)  
    def setHelmInfo( self,dataMap):
        self.resource_helm_data = dataMap
        
    def setHelmInfoValue( self, lst_value):
        self.resource_helm_data["values"] = [lst_value]
        
    def getHelmInfo( self ):
        return self.resource_helm_data
            
    
        
        
        
        
    
#app = App()
release_config_data = {
    "chart": "nginx",
    "name": "cdktf-nginx10",   #<<== resource.instances.attribute.id | attrribute.name || resource.instance.name
    "create_namespace" : True,
    "namespace" : "cdktf-nginx",
    "repository" : "https://charts.bitnami.com/bitnami",
    "version": "15.0.0",
    #"values": []
}


release_tomcat_config_data = {
    "chart": "tomcat",
    "name": "cdktf-tomcat",   #<<== resource.instances.attribute.id | attrribute.name || resource.instance.name
    "create_namespace" : True,
    "namespace" : "cdktf-nginx",
    "repository" : "https://charts.bitnami.com/bitnami",
    "version": "10.9.2",
    "values": []
}


release_apache_config_data = {
    "chart": "apache",
    "name": "cdktf-apache10",   #<<== resource.instances.attribute.id | attrribute.name || resource.instance.name
    "create_namespace" : True,
    "namespace" : "cdktf-nginx",
    "repository" : "https://charts.bitnami.com/bitnami",
    "version": "9.6.1",
    #"values": []
}



release_velero_config_data = {
    "chart": "velero",
    "name": "velero",   #<<== resource.instances.attribute.id | attrribute.name || resource.instance.name
    "create_namespace" : True,
    "namespace" : "velero",
    "repository" : "https://vmware-tanzu.github.io/helm-charts/",
    "version": "2.30.0",
    "values": [],
    "irsa": {}
}


from ClusterInfoYaml import * 


nCompany = 1000
InfraYaml = HelmInfraYaml(nCompany)


addon_name = "external_dns"
infrayaml = InfraYaml.view_yaml(addon_name)


#release_tomcat_config_data[values] = infrayaml
release_tomcat_config_data["values"] = [infrayaml]
print( "release_tomcat", release_tomcat_config_data)



helm = helmClass( )
#helm.helm_Input_data2( "helm_name_thing", "./values3.yaml",     **release_config_data  )
helm.helm_Input_data( "helm_name_tomcat",    **release_tomcat_config_data  )
#helm.helm_Input_data2( "helm_name_apache", "./values4.yaml",    **release_apache_config_data  )
#helm.helm_Input_data2( "velero",                None,           **release_velero_config_data  )
helm.deploy(True)






### ==>  python shell.py 수행

        
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
        
        

        # result = 0
        # START, END = 0, 100000000
        # result = Queue()
        
        # th1 = Process(None, work, args=(1, START, END//2, result))
        #th1.start()
        
        #cmd = ShellCommandDB(100, 1000, 'cdktf deploy')
        #sleep(10)
        #print( "return =======>" ,cmd.Excute_Retrun_Value() )
        
#         result = ""
        
#         #print( "reuslt: ", result)    

# def work(id, start, end, result):
#     total = 0        
#     print( "work thread started")
#     cmd = ShellCommandDB(100, 1000, ' pwd ')
#     cmd.Excute_Retrun_Value()
                         
#     cmd = ShellCommandDB(100, 1000, 'cdktf deploy --auto-approve  ' )
#     cmd.Excute_Retrun_Value()
    
    
#     #cmd.Excute_Complted_Retrun_Value()
#     #cmd.Excute_popen_Retrun_Value()  ## 에러 setRawMode EIO        