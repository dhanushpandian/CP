a=list(map(int,input().split(',')))
# print(a,type(a))

def norep(a:list[int]) -> int:
    d={}
    for i in a:
        d[i]=d.get(i,0)+1
    for i in a:
        if d[i]==1:
            return i
    return -1

print(norep(a))
