import os
import yaml

from ClusterInfoAddOne1_Helm import *
from ClusterInfoAddOne2_Helm import *


class Company:
    company_list = {
        "1000": {
            "dev": {
                "amazon_eks_coredns",
                "amazon_eks_kube_proxy",
                "external_dns"
            },
            "stg":{
                "amazon_eks_coredns"
                "amazon_eks_vpc_cni"
            }
        }
    }
    
    def __init__(self, nCompany):
        self.sCompanyname = self.company_list[nCompany]


class ClusterInfo:
    nCompany = 0
    awsRegion = "ap-northeast-2"
    clsuterName = "eks-cluster-zum"
    eks_version = "1.24"
    workSpaceEnv = "dev"
    nodeGroupOpsSystem = "ops-system"
    nodeGroupAppsSystem = "apps-system"

    opsManageDomain = "zumInternal.com"
    appServiceDomain = "zum.com"

    ingressClassName = "alb"
    storageClassName = "gp3"

    def __init__(self, nCompany):
        self.nCompany = nCompany

    def getCompany(self):               return self.nCompany
    def getAWSRegion(self):             return self.awsRegion
    def getClusterName(self):           return self.clsuterName
    def getEKSVersion(self):            return self.eks_version
    def getWorkSpaceENV(self):          return self.workSpaceEnv
    def getNodeGroupSystem(self):       return self.nodeGroupOpsSystem
    def getNodeGroupAppsSystem(self):   return self.nodeGroupAppsSystem
    def getOpsManageDomain(self):       return self.opsManageDomain
    def getAppSericeDomain(self):       return self.appServiceDomain
    def getIngressClassName(self):      return self.ingressClassName
    def getStorageClassName(self):      return self.storageClassName




class HelmInfraYaml:
    InfraYaml = None
    objClusterInfo = None    
    
    def __init__(self, nCompany):
        self.nCompany = nCompany
        self.objClusterInfo = ClusterInfo(self.nCompany)
        

    def GetInfraYaml(self, addOnName):
        if addOnName == "external_dns":
            externalDNS = external_dns(self.objClusterInfo)
            self.InfraYaml = externalDNS.GetInfraYaml()
        elif addOnName == "alb_controller":
            albController = alb_controller(self.objClusterInfo)
            self.InfraYaml = albController.GetInfraYaml()

        return self.InfraYaml
    
    def create_helm_value_files(self, addon_name):
        base_dir = "./helm_value"

        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        addon_dir = os.path.join(base_dir, addon_name)
        if not os.path.exists(addon_dir):
            os.makedirs(addon_dir)

        addon_file = os.path.join(addon_dir, "values.yaml")
        infra_yaml = yaml.dump(self.GetInfraYaml(addon_name))

        with open(addon_file, "w") as file:
            file.write(infra_yaml)


    def view_yaml(self, addon_name):
        infra_yaml = yaml.dump(self.GetInfraYaml(addon_name))
        print(infra_yaml)
        return infra_yaml



nCompany = 1000
InfraYaml = HelmInfraYaml(nCompany)

def main():
    addon_name = "external_dns"
    InfraYaml.view_yaml(addon_name)
    InfraYaml.create_helm_value_files(addon_name)

    # 전체 보기
    if addon_name == "all":
        addon_names = list(InfraYaml.objClusterInfo.sCompanyname[InfraYaml.objClusterInfo.getWorkSpaceENV()])
        for addon in addon_names:
            InfraYaml.view_yaml(addon)
            InfraYaml.create_helm_value_files(addon)

main()
