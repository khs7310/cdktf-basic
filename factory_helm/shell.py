
import subprocess


# simple_result = subprocess.call( 'cdktf deploy --auto-approve ', shell=True)
# #simple_result = subprocess.call( 'ls -al', shell=True)

# print("----------------")
# print("simple_result = %d ", simple_result)   # error 127 success 0


#########2 ###########

# usr_cmd = 'cdktf deploy --auto-approve'
# output_result = subprocess.check_output( usr_cmd, shell=True)
# print("-----subprocess out------")
# print("sub_process = %s ", output_result)






#########3 ###########

# print("-------------------- echo  --------")
# #subprocess.check_output(["echo", "Hello World!"])
# out_result2 = subprocess.check_output("cdktf deploy --auto-approve", shell = True )
# print("out_result2= ", out_result2)

#########4 ###########




#print("-------------------- echo  --------")
#subprocess.check_output(["echo", "Hello World!"])
#out_result2 = subprocess.check_output("lsa -al", 
# out_result2 = subprocess.check_output("cdktf deploy --auto-approve", 
#                     stderr=subprocess.STDOUT,   
#                     shell = True )
# print("out_result2= ", out_result2)
##  subprocess.CalledProcessError: Command 'lsa -al' returned non-zero exit status 127. 표시해줌


#print("-------------------- stderr --------")


# output= subprocess.check_output( "cdktf deploy --auto-approve",    
#                 stderr=subprocess.STDOUT,   
#                 shell=True)
# print ("kubectl get po : ", output)                

# """

#print("==============two ================")

# cmd = "cdktf deploy --auto-approve"
# ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
# output = ps.communicate()[0]
# print(output)






result = subprocess.run(["python", "main2.py"], capture_output=True, text=True)

print(result.stdout)

print(result.stdout)