class User:
    users={}
    def __init__(self,username=None,uid=None,password=None):
        self.username=username
        self.uid=uid
        self.password=password
    def save(self):
        User.users[self.uid]=[self.username,self.password]
    def __str__(self) -> str:
        return self.username


class Parti(User):
    scores={}
    def __init__(self, username=None, uid=None, password=None,clgname=None,rollno=None):
        super().__init__(username, uid, password)
        self.clgname=clgname
        self.rollno=rollno
        Parti.scores[self.uid]=[]
        print("User "+self.username+" created!")
    
class Quizr(User):
    quizes={}
    def __init__(self, username=None, uid=None, password=None,company=None):
        super().__init__(username, uid, password)
        self.company=company
        print("User "+self.username+" created!")
    def addquiz(self,type,domain):
        Quizr.quizes[domain]=[]
        if type =="mcq":
            n=int(input("enter number of questions: "))
            qns=[]
            for i in range(n):
                d={}
                x=input("enetr question ",i+1, ": ")
                os=input("eneter options: ")
                crt=input("emter correct ans : ")
                d[i+1]=[x,os,crt]
                qns.append(d)




def participant(uid):
    while True:
        opt=int(input("enter options \n 1> view quiz \n 2> see scores \n 3> view by company \n 4> edit profile \n 5> exit"))
        if opt==1:
            x=int(input("enter 1> see all quizes 2> see based on domain"))
            if x==1:
                print(Quizr.quizes)
            elif x==2:
                do=input("enetr domain name : ")
                print(Quizr.quizes[do])
        elif opt==2:
            pass
        elif opt==3:
            pass
        elif opt==4:
            pass
        elif opt==5:
            print("Exiting !")
        else:
            print("Invallid ")
        
def quizzer(uid):
    while True:
        opt=int(input("Enter options 1> view quizs 2> add new quiz 3>modify 4> delete quiz"))
        if opt==2:
            t=input("type: ")
            dom=input("domain: ")
            Quizr.addquiz(t,dom)        


while True:
    print("==========================================")
    print("Enter Option 1> Login 2> Register")
    lr=int(input())
    if lr==1:
        print("Login as Enter Option 1 or 2 \n 1> participant 2> quizerr")
        opt=int(input())
        if opt==1:
            pid=input("enter userid : ")
            ppass=input("enter pasword : ")
            if User.users[pid][1]==ppass:
                print("Logged in as "+User.users[pid][0])
                participant(pid)
            else:
                print("Invalid Creds")
        elif opt==2:
            pid=input("enter userid : ")
            ppass=input("enter pasword : ")
            if User.users[pid][1]==ppass:
                print("Logged in as "+User.users[pid][0])
                quizzer(pid)
            else:
                print("Invalid Creds")

    elif lr==2:
        print("Register as Enter Option 1 or 2 \n 1> participant 2> quizerr ")
        opt=int(input())
        if opt==1:
            pn=input("enter name : ")
            pid=input("enter userid : ")
            ppass=input("enter pasword : ")
            pclg=input("enter clg name : ")
            prolno=input("enter rollno : ")
            p=Parti(pn,pid,ppass,pclg,prolno)
            p.save()
        elif opt==2:
            pn=input("enter name : ")
            pid=input("enter userid : ")
            ppass=input("enter pasword : ")
            pcomp=input("enter company name : ")
            p=Quizr(pn,pid,ppass,pcomp)
            p.save()
            print(User.users[p.uid])
        else:
            print("invalid input! ")

    else:
        print("invalid input")




