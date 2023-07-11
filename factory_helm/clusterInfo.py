
import os
import yaml

class Company():
    
    company_list = {
        "1000" : {
            "dev" : {
                "amazon_eks_coredns",
                "amazon_eks_kube_proxy",
                "external_dns"
            # amazon_eks_vpc_cni      = {}
            # amazon_eks_ebs_csi_driver = { }
            # amazon_eks_efs_csi_driver = { }
            # self_managed_coredns    = {}
            # kube_prometheus_stack   = {}
            # alb_controller          = {}
            # external_dns            = {"10.1.2" :{ "eks_version" : ["1.24", ], "IRSA" : True, "domain" : ["korea.com", "expose.com"] } } # cluster_domain_name
            # external_secret         = { } # cluster_domain_name
            # cluster_autoscaler      = {}            
            # cert_manager            = {}
            # aws_for_fluentbit       = {}
            # argocd                  = {}
            # argo_rollouts           = {}
            
           }
        }
    }
    def __init__(self, nCompany):
        self.sCompanyname = self.company_list[nCompany]    

class ClusterInfo():     
    nCompany            = 0
    awsRegion           = "ap-northeast-2"
    clsuterName         = "eks-cluster-zum"
    eks_version         = "1.24"
    workSpaceEnv        = "dev"
    nodeGroupOpsSystem  = "ops-system"
    nodeGroupAppsSystem = "apps-system"
    
    opsManageDomain     = "zumInternal.com"   
    appServiceDomain    = "zum.com"
    
    ingressClassName    = "alb"
    storageClassName    = "gp3"    
    
    def __init__(self, nCompany):
        self.nCompany = nCompany     
        
    def getCompany(self): return self.nCompany
    def getAWSRegion(self): return self.awsRegion
    def getClusterName(self): return self.clsuterName
    def getEKSVersion(self): return self.eks_version
    
    
    def getWorkSpaceENV(self): return self.workSpaceEnv
    def getNodeGroupSystem(self): return self.nodeGroupOpsSystem
    
    def getNodeGroupAppsSystem(self): return self.nodeGroupAppsSystem
    def getOpsManageDomain(self): return self.opsManageDomain
    def getAppSericeDomain(self): return self.appServiceDomain
    def getIngressClassName(self): return self.ingressClassName
    def getStorageClassName(self): return self.storageClassName


class AddOn1():   
    
    amazon_eks_coredns      = {}
    amazon_eks_kube_proxy   = {}
    amazon_eks_vpc_cni      = {}
    amazon_eks_ebs_csi_driver = { }
    amazon_eks_efs_csi_driver = { }
    self_managed_coredns    = {}
    kube_prometheus_stack   = {}
    alb_controller          = {}
    external_dns            = {
                                "10.1.2" :{ "eks_version" : ["1.24", ], "IRSA" : True, },
                                "10.3.2" :{ "eks_version" : ["1.24", ], "IRSA" : True, },
                                "10.5.2" :{ "eks_version" : ["1.25", ], "IRSA" : True, }, 
                                
                               
                               } # cluster_domain_name
    external_secret         = { } # cluster_domain_name
    cluster_autoscaler      = {}            
    cert_manager            = {}
    aws_for_fluentbit       = {}
    argocd                  = {}
    argo_rollouts           = {}


class Addon2():
    
    
    keycloak = { "10.1.2" : ["1.24", ],
                "10.1.3" : ["1.25",]
    }
        
    grafana              = { }
    velero               = {}
    jenkins             = {}
    alb_tomcat          = {}
    alb_nginx           = {}
    alb_apache          = {}        
    kubernetes_dashboard= {}        
    gitlab              = {}        
    nginx_tomcat        = {}        
    nginx_apache        = {}
    nginx_nginx         = {}
    


class external_dns():

    company_eks_version = ""
    objClusterInfo = None
    objAddOn1 = None
    InfraYaml = None
    fiexedApplyEKSVersion = ""
    def __init__(self, objClusterInfo:ClusterInfo,  objAddOn1:AddOn1 ):
        self.objClusterInfo = objClusterInfo
        self.objAddOn1 = objAddOn1
        
        self.fiexedApplyEKSVersion = self.FindEKSHelmVersion(self)
        
        
    
    def FindEKSHelmVersion(self):
        latest_eks_version = None
        for version in self.objAddOn1.external_dns.keys():
            eks_version_list = self.objAddOn1.external_dns[version].get("eks_version")
            if eks_version_list:
                max_version = max(eks_version_list)
                if latest_eks_version is None or max_version > latest_eks_version:
                    latest_eks_version = max_version
        
        print(" latest_eks_version:", latest_eks_version)
        return latest_eks_version

    
    def GetInfraYaml(self):
        
        
        yaml = """
aws:
  region: ${self.objClusterInfo.getRegionName()}
  zoneType: public

domainFilters:
  - ${self.objClusterInfo.getAppSericeDomain()}
policy: upsert-only 
registry: txt

"""
# txtOwnerId: ${txtOwnerId}              
        
        
        
        return self.InfraYaml


class HelmInfraYaml():

    InfraYaml = None
    objClusterInfo = None
    
    def __init__(self, nCompany):
        self.nCompany = nCompany  
        self.objClusterInfo = ClusterInfo( self.nCompany)
        self.objAddOne1 = AddOn1( )
        
    def GetInfraYaml(self, addOnName:str, InputYaml):
        if addOnName == "external_dns":
            externalDNS  = external_dns(self.objClusterInfo,self.objAddOne1)
            self.InfraYaml = externalDNS.GetInfraYaml()
            
            
        return self.InfraYaml 
        
class HelmCustomerYaml():

    CustomerYaml = None
    def __init__(self, nCompany):
        self.nCompany = nCompany  
        
    def GetCustomerYaml(self):
        return self.CustomerYaml 
    
    
    
    
nCompany = 1000
InfraYaml =   HelmInfraYaml(nCompany)
print("InfraYaml:", InfraYaml)
CustomerYaml =   HelmCustomerYaml(nCompany)

TotalYaml = CustomerYaml + InfraYaml 





  
    
    
    
    
    