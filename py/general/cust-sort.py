#arr of lbh or various boxes
arr= [(1,10,3),(2,13,40),(11,2,3),(4,25,6),(11,2,30)]
arr.sort()
print(arr)

def area(X):
    L,B,H = X
    return L*B

print(sorted(arr,key=area))


print(sorted(arr,key=lambda x: max(x[0]*x[1],x[1]*x[2],x[0]*x[2])))