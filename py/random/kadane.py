a=list(map(int,input().split(',')))
c=a[0]
ans=a[0]
for i in a[1:]:
    c=max(i,c+i)
    ans=max(ans,c)
print(ans)