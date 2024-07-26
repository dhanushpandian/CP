from usertypes import JobProvider, Seeker


while True:
    print("""
Enetr Option 
1> Login
2> Register
3> Exit""")
    option=int(input("Enter Option: "))
    if option==2:
        print("Enter User Type 1> Seeker 2> JobProvider")
        ut=int(input())
        print("Enetr Username: ")
        u=input()
        print("Enter Password: ")
        p=input()
        if ut==1:
            print("Enter Resume: ")
            r=input()
            print("Enter Skills with commas : ")
            s=input().split(",")
            s=[i.strip() for i in s]
            s=[i for i in s if i]
            Seeker(u,p,r,s).save()
        elif ut==2:
            print("Enter Company: ")
            c=input()
            print("Enter Job Title: ")
            jt=input()
            print("Enter Job Description: ")
            jd=input()
            JobProvider(u,p,c,jt,jd).save()
        else:
            print("Invalid User Type")
    elif option==1:
        print("Enter Option 1> Seeker 2> JobProvider")
        ut=int(input())
        if ut == 1:
            print("Enter Username: ")
            u=input()
            print("Enter Password: ")
            p=input()
            if u in Seeker.seekers and Seeker.seekers[u][0]==p:
                print("Seeker Found")
                print("Resume: ",Seeker.seekers[u][0])
                print("Skills: ",Seeker.seekers[u][1])
            else:
                print("Seeker Not Found")
        elif ut==2:
            print("Enter Username: ")
            u=input()
            print("Enter Password: ")
            p=input()
            if u in JobProvider.jobproviders and JobProvider.jobproviders[u][0]==p:
                print("Job Provider Found")
                print("Company: ",JobProvider.jobproviders[u][0])
                print("Job Title: ",JobProvider.jobproviders[u][1])
                print("Job Description: ",JobProvider.jobproviders[u][2])
            else:
                print("Job Provider Not Found")
            
        else:
            print("Invalid User Type")

    elif option==3:
        print("Exiting....")
        break
    else:
        print("Invalid Option")
        

        