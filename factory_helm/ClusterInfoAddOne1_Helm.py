
from ClusterInfoAddOne import *

class external_dns(AddOnBase):
    
    def __init__(self, _objClusterInfo):
        super().__init__(str(self.__class__.__name__))
        self.objClusterInfo = _objClusterInfo
        
    
    def GetInfraYaml(self):
        infra_yaml = {
            "aws": {
                "region": self.objClusterInfo.getAWSRegion(),
                "zoneType": "public"
            },
            "domainFilters": [self.objClusterInfo.getAppSericeDomain()],
            "policy": "upsert-only",
            "registry": "txt",
            "region": self.objClusterInfo.getAWSRegion(),
            
        }
        return infra_yaml


class alb_controller(AddOnBase):
    
    def __init__(self, _objClusterInfo):
        super().__init__(str(self.__class__.__name__))
        self.objClusterInfo = _objClusterInfo
    
    def GetInfraYaml(self):
        infra_yaml = {
            "clusterName": self.objClusterInfo.getClusterName(),
            "region": self.objClusterInfo.getAWSRegion(),            
            "image": {
                "repository": "repository"
            }
        }
        return infra_yaml