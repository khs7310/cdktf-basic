


from constructs import Construct
from cdktf import App, TerraformStack




class MakeResoureFactory( ):
    #MyStack myStack
    #def __init__(self, scope: Construct, ns: str, MyStack: stack): 
    def __init__(self, scope: Construct, ns: str): 
        return 0
    def create_resource_inner(oj_name):
        app = App()
        # obj = MyStack(TerraformStack)
        
        
        AwsProvider(self, "AWS", region="us-west-1")

        instance = Instance(self, "compute",
                            ami="ami-01456a894f71116f2",
                            instance_type="t2.micro",
                            )
        
        

    def create_resource(oj_name):
        return
         



class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here


app = App()
MyStack(app, "learn-cdktf")

app.synth()
