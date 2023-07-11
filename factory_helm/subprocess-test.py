#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack



import json
import yaml
from time import sleep
from multiprocessing import Process, Queue

from ShellCommand import ShellCommandDB
import subprocess
import shlex

return_shlex = shlex.split('cdktf deploy --auto-apporve')
print("return_shlex:", return_shlex[0])
sCommand = "cdktf synth"
sCommand = "cdktf deploy --auto-approve"
print("-->",shlex.split(sCommand))
#subprocess.run( ['cdktf','diff', ],text=True, shell=True, capture_output=True )

subprocess.run( 
                                        shlex.split(sCommand),                                        
                                        #capture_output=True, 
                                        text=True,
                                        shell=False)


#print( "return", return_output)
#print( "out", return_output.stderr)
#print( "error", return_output.stdout)

    
    