a=[1,2,3,4,5]
print(a)
e=[i for i in a if i%2==0]
o=[i for i in a if i%2!=0]
a=e+o
for  i in a:
    print(i,    end=' ')