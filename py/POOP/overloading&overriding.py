#same name different parameters is called overloading
#python dont have overloading
#but has Method Overriding
#Method Overriding: same name same parameters in parent and child class

class Parent:
    def show(self):
        print("Parent Class")

class Child(Parent):    
    def show(self):
        print("Child Class")

a=Child()
a.show()  