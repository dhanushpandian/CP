#python Object Oriented Programming

from car import Car

car1=Car("Toyota", "Corolla", 2015, "White")
car2=Car("Honda", "Civic", 2018, "Black")
print(car1)
print(car2.brand)

car1.drive()    
car2.stop()

car3=Car()
print(car3)