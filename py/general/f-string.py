a="dhanush"
b="pandian"

a="My name is {} {}".format(a,b)
print(a)

person={"name":"dhanush","age":21}

a="My name is {name} and age is {age}".format(**person)
print(a)

a=f"My name is {person['name'].upper()} and age is {person['age']}"
print(a)

x=[10,20]
a=f"{x[0]} + {x[1]} = {x[0]+x[1]}"
print(a)

for i in range(1,11):
    print(f"Square of {i} is {i**2}")

pi=3.14159265359
print(f"Value of pi is {pi:.4f}")

from datetime import datetime  
today = datetime.today()
bday=datetime(2003,5,24)
print(f"Today is {today}")
print(f"Today is {today:%B %d, %Y}")
print(f"My birthday is {bday}")
print(f"My birthday is {bday:%B %d, %Y}")

