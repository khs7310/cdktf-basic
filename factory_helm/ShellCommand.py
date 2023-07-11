
import subprocess, shlex

class ShellCommandDB:
    def __init__(self,nID, nCompany, sCommand) :
        self.nID        = nID
        self.nCompany   = nCompany
        self.sCommand   = sCommand
        self.nCommand_nReturn = -1
        self.sCommand_OUTPUT = ''
        self.sCommand_Fail_OUTPUT = ''
        self.bCommand_ApplyOK = False
        self.bReturn_ApplyOK   = False

    def Excute_Retrun_Only(self) :
        self.nCommand_nReturn = subprocess.call( 
                                        self.sCommand, 
                                        shell=True)
        self.bCommand_ApplyOK = True

        #print("리턴결과:", self.nCommand_nReturn)
        

        if(self.nCommand_nReturn == 0) :
            self.bReturn_ApplyOK = True          
        else :
            self.bReturn_ApplyOK = False          

        return self.nCommand_nReturn

    # def Excute_Return_String(self) :
    #     return self.sCommand_OUTPUT

    def Excute_Return_Fail_Value(self) :
        if( self.bReturn_ApplyOK) :
            if( self.nCommand_nReturn == 0 ) :
                return self.sCommand_Fail_OUTPUT

        return self.sCommand_Fail_OUTPUT
    

    def Excute_Retrun_Value(self) :

        try:
            self.sCommand_OUTPUT = subprocess.call( 
                                        self.sCommand, 
                                        stderr=subprocess.STDOUT,
                                         
                                        shell=True)
            self.bCommand_ApplyOK = True

            if(self.nCommand_nReturn == 0) :
                self.bCommandOK = True
                
                          
                
            return self.sCommand_OUTPUT

        except:

            self.sCommand_Fail_OUTPUT = self.sCommand_OUTPUT
            self.bCommandOK = True
            self.nCommand_nReturn = 1
            ##   returned non-zero exit status 127 Parser
        
        return self.sCommand_OUTPUT


    def Excute_Complted_Retrun_Value(self) :

        try:
            print("command:", self.sCommand)
            self.sCommand_OUTPUT = subprocess.run( 
                                        self.sCommand, 
                                        capture_output=True,
                                        stderr=subprocess.STDOUT,
                                        shell=True)
            self.bCommand_ApplyOK = True

            if(self.nCommand_nReturn == 0) :
                self.bCommandOK = True
                
                          
                
            return self.sCommand_OUTPUT

        except:

            self.sCommand_Fail_OUTPUT = self.sCommand_OUTPUT
            self.bCommandOK = True
            self.nCommand_nReturn = 1
            ##   returned non-zero exit status 127 Parser
        
        return self.sCommand_OUTPUT



    def Excute_Capture_All_Value(self) :

        try:
            self.sCommand_OUTPUT = subprocess.run( 
                                    shlex.split(self.sCommand), 
                                    #stderr=subprocess.STDOUT,
                                    # 미사용
                                    #capture_output=True, 
                                    capture_output=False, 
                                    text=True,
                                    shell=False)
            #print( "shell command:", self.sCommand_OUTPUT)
            self.bCommand_ApplyOK = True

            if(self.nCommand_nReturn == 0) :
                self.bCommandOK = True
                
            #print("scommand: ", self.sCommand)
            #print("out===>: ", self.sCommand_OUTPUT.stdout)
            #print("err===>", self.sCommand_OUTPUT.stderr)
            #print("returncode:====>", self.sCommand_OUTPUT.returncode)  # 127
                
            return self.sCommand_OUTPUT

        except:

            self.sCommand_Fail_OUTPUT = self.sCommand_OUTPUT
            self.bCommandOK = True
            self.nCommand_nReturn = 1
            ##   returned non-zero exit status 127 Parser
            print("command: ", "exception")
        
        return self.sCommand_OUTPUT



# cmd = ShellCommandDB(100, 1000, ' pwd ')
# cmd.Excute_Retrun_Value()
# cmd = ShellCommandDB(100, 1000, 'cdktf deploy --auto-apply  ' )

# cmd.Excute_Retrun_Value()


# ls2 = subprocess.run(['m', '', ''], capture_output=True, text=True, shell=True)

# # ls2: CompletedProcess(args=['m', '', ''], returncode=127, stdout='', stderr=': 1: m: not found\n')

# print("out: ", ls2.stdout)
# print("err", ls2.stderr)
# print("returncode:", ls2.returncode)  # 127



### 참고 
# shell=True 를 사용할 때, 중간에 subprocess가 /bin/sh 를 통해서 실행된다.
# 그래서 실제 cmd 명령어를 사용한 pid에서 한번 더 subprocess가 생성되어 pid가 
# 달라지게 되는 경우가 있다.

# ex) python manage.py runserver를 실행한 pid는 3030인데, 
# /bin/sh python mana.py runserver가 3030이 되고, 
# 실제 runserver를 실행한 pid는 3031이 되는경우