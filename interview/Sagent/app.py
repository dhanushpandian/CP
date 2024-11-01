import datetime
class User: 
    def __init__(self,name,uid):
        self.name=name
        self.id= uid
rooms={1:["Taj","100000","1","1"],2:["Hilton","150000","2","5"]}
bookings={1:["10-9-24"]}
def add_room():
    print("enter Hotel name,Fare,type (1 for deluxe,2 for Family 3 for standard):, Availability ")
    inp=input()
    a=inp.split(',')
    rooms[len(rooms)+1]=a



def display_all():
    print("\nRooms Available:")
    for i in rooms:
        print(i,") hotel name:",rooms[i][0],"Fare:",rooms[i][1],"Type: ",rooms[i][2],"Available:",rooms[i][3])
    
def view_based():
    pass

def display_bookings():
    print("\nDisplaying Bookings:")
    for i in bookings:
        for j in bookings[i]:
            print(i,"Hotel: ",rooms[i][0],"Price: ",rooms[i][1],"Date:",j)

def book(bid,dat):
    #print(bookings)
    if int(rooms[bid][3]) > 0:
        if bid in bookings and dat in bookings[bid]:
            print("The Room is already booked")
        else:
            if bid not in bookings:
                bookings[bid]=[]
            a=bookings[bid]
            a.append(dat)
            bookings[bid]=a
            print("Room Booked on",dat,"payment to be made as Advance:",int(rooms[bid][1])*0.5)
            print("Redirectring to Payment Gateway......")
            rooms[bid][3]=str(int(rooms[bid][3])-1)
    else:
        print("Rooms Not available")

def cancel_date(x,y):
    print("cancelled booking",rooms[x][0],"Date:",y)
    a=[]
    for i in bookings[x]:
        if i != y:
            a.append(i)
    bookings[x]=a
    xx=int(rooms[x][1])*0.5
    print("Advance Made of rupes",xx,"will be refunded shortly")
    print("Availablle rooms=",rooms[x][3])

    


def cancel_booking(x):
    print("cancelled booking",bookings[x])
    l=len(bookings[x])
    del bookings[x]
    xx=int(rooms[x][1])*0.5
    rooms[x][3]=str(int(rooms[x][3])+1)
    print("Advance Made of rupes",xx*l,"will be refunded shortly")
    print("Availablle rooms=",rooms[x][3])

while True:
    o1=int(input("\n 1 for Admin \n 2 for User \n"))
    if o1==1:
        print("\n enter 1 for adding room\n2 for viewing rooms \n 3 for view rooms based on parameters \n 4 for view bookings")
        o2=int(input())
        if o2==1:
            add_room()
        elif o2==2:
            display_all()
        elif o2==3:
            pass
        elif o2==4:
            display_bookings()

    elif o1==2:
         print("\n enter 1 for Viewing rooms\n2 for view rooms based on parameters  \n 3 for Booking rooms\n 4 for display bookings \n 5 for Cancelling a booking")
         o2=int(input())
         if o2==1:
             display_all()
         elif o2==2:
             view_based()
         elif o2==3:
             bid=int(input("\n Enter the room id to book:"))
             dat=input("enter date u want to book:")
             book(bid,dat)
         elif o2==4:
             display_bookings()
         elif o2==5:
              display_bookings()
              x=int(input("enter the hotel id to cancel"))
              y=input("Enter date to cancel")
              cancel_date(x,y)
            #   cancel_booking(x)
              
        



            
        

    