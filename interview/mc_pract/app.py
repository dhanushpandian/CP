 #from usertypes import User, Seeker, JobProvider
class User:
    users = {}

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def save(self):
        User.users[self.username] = self.password
        print("User Has been added!")


class Seeker(User):
    seekers = {}

    def __init__(self, username: str, password: str, resume: str, skills: list):
        super().__init__(username, password)
        self.resume = resume
        self.skills = skills

    def save(self):
        super().save()
        Seeker.seekers[self.username] = [self.resume, self.skills]
        print("Seeker Data Has been added!")


class JobProvider(User):
    jobproviders = {}

    def __init__(self, username: str, password: str, company: str, jobtitle: str, jobdesc: str, location: str):
        super().__init__(username, password)
        self.company = company
        self.jobtitle = jobtitle
        self.jobdesc = jobdesc
        self.location = location

    def save(self):
        super().save()
        JobProvider.jobproviders[self.username] = [self.company, self.jobtitle, self.jobdesc, self.location]
        print("JobProvider Data Has been added!")


def seeker(u:str):
    while True:
        print("""
    Enter Option
              1> See all Jobs
              2>Search Job With skills
              3> Search Job with Location
              4> Exit""")
        option = int(input("Enter Option: "))
        if option==1:
            print("All Jobs")
            for i in JobProvider.jobproviders:
                print("Company: ", JobProvider.jobproviders[i][0])
                print("Job Title: ", JobProvider.jobproviders[i][1])
                print("Job Description: ", JobProvider.jobproviders[i][2])
                print("Location: ", JobProvider.jobproviders[i][3])
                print("====================================")
        elif option==2:
            print("Your Skills:",Seeker.seekers[u][1])
            print("Jobs with your skills")
            for j in Seeker.seekers[u][1]:
                for i in JobProvider.jobproviders:
                    if j in JobProvider.jobproviders[i][2]:
                        print("Company: ", JobProvider.jobproviders[i][0])
                        print("Job Title: ", JobProvider.jobproviders[i][1])
                        print("Job Description: ", JobProvider.jobproviders[i][2])
                        print("Location: ", JobProvider.jobproviders[i][3])
                        print("====================================")
        elif option==3:
            print("Enter Location: ")
            l=input()
            print("Jobs with your Location")
            for i in JobProvider.jobproviders:
                if l in JobProvider.jobproviders[i][3]:
                    print("Company: ", JobProvider.jobproviders[i][0])
                    print("Job Title: ", JobProvider.jobproviders[i][1])
                    print("Job Description: ", JobProvider.jobproviders[i][2])
                    print("Location: ", JobProvider.jobproviders[i][3])
                    print("====================================")
        elif option==4:
            print("Exiting....")
            break
        else:
            print("Invalid Option")
        
while True:
    print("====================================")
    print("""
Enter Option 
1> Login
2> Register
3> Exit""")
    option = int(input("Enter Option: "))
    if option == 2:
        print("Enter User Type 1> Seeker 2> JobProvider")
        ut = int(input())
        print("Enter Username: ")
        u = input()
        print("Enter Password: ")
        p = input()
        if ut == 1:
            print("Enter Resume: ")
            r = input()
            print("Enter Skills with commas : ")
            s = input().split(",")
            s = [i.strip() for i in s]
            s = [i for i in s if i]
            se = Seeker(u, p, r, s)
            se.save()
        elif ut == 2:
            print("Enter Company: ")
            c = input()
            print("Enter Job Title: ")
            jt = input()
            print("Enter Job Description: ")
            jd = input()
            print("Enter Location: ")
            l = input()
            jp = JobProvider(u, p, c, jt, jd, l)
            jp.save()
        else:
            print("Invalid User Type")
    elif option == 1:
        print("Enter Option 1> Seeker 2> JobProvider")
        ut = int(input())
        if ut == 1:
            print("Enter Username: ")
            u = input()
            print("Enter Password: ")
            p = input()
            if u in User.users and User.users[u] == p:
                if u in Seeker.seekers:
                    print("Seeker Found")
                    print("Resume: ", Seeker.seekers[u][0])
                    print("Skills: ", Seeker.seekers[u][1])
                    seeker(u)
                else:
                    print("Seeker Not Found")
            else:
                print("Invalid Username or Password")
        elif ut == 2:
            print("Enter Username: ")
            u = input()
            print("Enter Password: ")
            p = input()
            if u in User.users and User.users[u] == p:
                if u in JobProvider.jobproviders:
                    print("Job Provider Found")
                    print("Company: ", JobProvider.jobproviders[u][0])
                    print("Job Title: ", JobProvider.jobproviders[u][1])
                    print("Job Description: ", JobProvider.jobproviders[u][2])
                    print("Location: ", JobProvider.jobproviders[u][3])
                else:
                    print("Job Provider Not Found")
            else:
                print("Invalid Username or Password")
        else:
            print("Invalid User Type")
    elif option == 3:
        print("Exiting....")
        break
    else:
        print("Invalid Option")


