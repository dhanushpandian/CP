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
        
    
class Quizr(User):
    def __init__(self, username=None, uid=None, password=None,company=None):
        super().__init__(username, uid, password)
        self.company=company


u=User("a","A","A")
print(u)


u=Parti("a","A","A","rec",10)
print(u.rollno)
print(u)
    
u=Quizr("a","A","A","aa")
print(u.company)


    