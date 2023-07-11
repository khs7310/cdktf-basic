
import subprocess



# return_object = subprocess.run(['ls', '-l'], 
#                                stdout=subprocess.DEVNULL, 
#                                text=True,
#                                capture_output=True,
#                                stderr=subprocess.STDOUT)

# print ("return_object" , return_object )


#subprocess.run(["ls", "-l", "/dev/null"] )
#subprocess.run(["ls", "-l", "/dev/null"], capture_output=False)
ls = subprocess.run(['ls', '-alh'], capture_output=True, text=True).stdout.strip("\n")

print(ls)

#ls2 = subprocess.run(['cdktf', 'deploy', '--auto-approve'], capture_output=True, text=True).stdout.strip("\n")
#ls2 = subprocess.run(['m', '', ''], capture_output=True, text=True, shell=True).stdout.strip("\n")
ls2 = subprocess.run(['m', '', ''], capture_output=True, text=True, shell=True)

# ls2: CompletedProcess(args=['m', '', ''], returncode=127, stdout='', stderr=': 1: m: not found\n')

print("out: ", ls2.stdout)
print("err", ls2.stderr)
print("returncode:", ls2.returncode)  # 127

print("ls2:", ls2)
print("ls2_completionProcess:", ls2)



# simple_result = subprocess.call( 'cdktf deploy --auto-approve ', shell=True)
# #simple_result = subprocess.call( 'kls -al', shell=True)

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






# result = subprocess.run(["python", "main2.py"], capture_output=True, text=True)

# print(result.stdout)

# print(result.stdout)