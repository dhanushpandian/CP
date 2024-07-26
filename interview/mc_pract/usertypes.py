class User:
    users={}

    def __init__(self,username=str,password=str):
        self.username=username
        self.password=password
    
    def save(self):
        User.users[self.username]=self.password
        print("User Has been added!")
    

class Seeker(User):

    seekers={}

    def __init__(self, username=str, password=str,resume=str,skills=[]):
        super().__init__(username, password)
        self.resume=resume
        self.skills=skills

    def save(self):
        a=[self.resume,self.skills]
        Seeker.seekers[self.username]=a
        print("Seeker Data Has been added!")
    
class JobProvider(User):

    jobproviders={}

    def __init__(self, username=str, password=str,company=str,jobtitle=str,jobdesc=str,location=str):
        super().__init__(username, password)
        self.company=company
        self.jobtitle=jobtitle
        self.jobdesc=jobdesc
        self.location=location

    def save(self):
        a=[self.company,self.jobtitle,self.jobdesc,self.location]
        JobProvider.jobproviders[self.username]=a
        print("JobProvider Data Has been added!")
    
    
