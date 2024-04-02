list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
a="efr"
# Zip the two lists together
result = zip(list1, list2,a)

# print(result)

# print(list(result))  

for i,j,k in zip(list1, list2,a):
    print(i,j,k)