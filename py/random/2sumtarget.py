nums=list(map(int,input().split(',')))
target=int(input("Enter target: "))
d = {}
for i in nums:
    if i in d:
        print(i, d[i])  # found the pair
        break
    else:
        d[target - i] = i  # store the complement
