class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        if(self.head is None):
            self.head=Node(data,None)
            return
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=Node(data,None)
    
    def print(self):
        if self.head is None:
            print("empty")
            return
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)
            itr=itr.next
        print(llstr)

if __name__=='__main__':
    ll=Linkedlist()
    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    ll.insert_at_begining(3)
    ll.print()
    ll.insert_at_end(0)
    ll.print()