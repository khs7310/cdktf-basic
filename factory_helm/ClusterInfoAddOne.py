

class AddOn1:
    amazon_eks_coredns = {}
    amazon_eks_kube_proxy = {}
    amazon_eks_vpc_cni = {}
    amazon_eks_ebs_csi_driver = {}
    amazon_eks_efs_csi_driver = {}
    self_managed_coredns = {}
    kube_prometheus_stack = {}
    alb_controller = {}
    external_dns = {
        "10.1.2": {"eks_version": ["1.29"],        "IRSA": True, "valueFiles": "external_dns_10.1.2.values.yaml" },
        "10.3.2": {"eks_version": ["1.24","1.26"], "IRSA": True, "valueFiles": "external_dns_10.3.2.values.yaml" },
        "10.5.2": {"eks_version": ["1.28"],        "IRSA": True, "valueFiles": "external_dns_10.5.2.values.yaml" },
    }
    external_secret = {
        
        "40.1.2": {"eks_version": ["1.24"],         "IRSA": True, "valueFiles": "external_secret_40.1.2.values.yaml"},
        "40.3.2": {"eks_version": ["1.24","1.26"],  "IRSA": True, "valueFiles": "external_secret_40.3.2.values.yaml"},
        "40.5.2": {"eks_version": ["1.27"],         "IRSA": True, "valueFiles": "external_secret_40.5.2.values.yaml"},
    }
    cluster_autoscaler = {
        
        "140.1.2": {"eks_version": ["1.24"],        "IRSA": True, "valueFiles": "external_secret_140.1.2.values.yaml"},
        "140.3.2": {"eks_version": ["1.24","1.26"], "IRSA": True, "valueFiles": "external_secret_140.3.2.values.yaml"},
        "140.5.2": {"eks_version": ["1.25"],        "IRSA": True, "valueFiles": "external_secret_140.5.2.values.yaml"},
        
    }
    cert_manager = {}
    aws_for_fluentbit   = {}
    argocd              = {}
    argo_rollouts = {}



class AddOn2:
    keycloak = {
        "4.1.2": {"eks_version": ["1.24"],        "IRSA": True, "valueFiles": "keycloak_4.1.2.values.yaml"},
        "4.3.2": {"eks_version": ["1.24","1.26"], "IRSA": True, "valueFiles": "keycloak_4.3.2.values.yaml"},
        "4.5.2": {"eks_version": ["1.25"],        "IRSA": True, "valueFiles": "keycloak_4.5.2.values.yaml"},
    }
    grafana = {}
    velero = {}
    jenkins = {}
    alb_tomcat = {}
    alb_nginx = {}
    alb_apache = {}
    kubernetes_dashboard = {}
    gitlab = {}
    nginx_tomcat = {}
    nginx_apache = {}
    nginx_nginx = {}




class AddOnBase():
    company_eks_version = ""
    objClusterInfo = None
    objAddOn1 = None
    InfraYaml = None
    fixedApplyEKSVersion = ""

    def __init__(self,  obeject_helm_name):
        
        self.objHelmName = obeject_helm_name
        
        #print( "var:", vars(AddOn1) )
        self.fixedApplyEKSVersion = self.FindEKSHelmVersion()
        
    def FindEKSHelmVersion(self):
        latest_eks_version = None
        class_addon1_attrs = vars(AddOn1)
        class_addon2_attrs = vars(AddOn2)
        
        bAddOn1 = False
        addons = []
        exclude_attributes = ["__dict__", "__weakref__", "__doc__"]
        
        for attr_name, attr_value in class_addon1_attrs.items():            
            if not attr_name.startswith("__") and not callable(attr_value) and attr_name not in exclude_attributes:
                addons.append(attr_value)
                
                if attr_name == self.objHelmName : 
                    bAddOn1 = True
                    for version in attr_value.keys():
                        if "eks_version" in attr_value[version]:
                            eks_version_list = attr_value[version].get("eks_version")
                            if eks_version_list:
                                max_version = max(eks_version_list)
                                if latest_eks_version is None or max_version > latest_eks_version:
                                    latest_eks_version = max_version
            
                #if(attr_name == self.objHelmName ):
                     
        if bAddOn1 == False :                       
            for attr_name, attr_value in class_addon2_attrs.items():            
                if not attr_name.startswith("__") and not callable(attr_value) and attr_name not in exclude_attributes:
                    
                    if attr_name == self.objHelmName : 
                        bAddOn1 = True
                        for version in attr_value.keys():
                            if "eks_version" in attr_value[version]:
                                eks_version_list = attr_value[version].get("eks_version")
                                if eks_version_list:
                                    max_version = max(eks_version_list)
                                    if latest_eks_version is None or max_version > latest_eks_version:
                                        latest_eks_version = max_version
                
        
        print("latest_eks_version:", latest_eks_version)
        return latest_eks_version

    
    def GetInfraYaml(self):
        raise NotImplementedError("Subclasses must implement GetInfraYaml")


    
    
