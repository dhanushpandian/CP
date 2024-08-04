print("ENTER NUM:")
arr=list(map(int,input()))
print(arr)
ans=[]
for i in range(len(arr)-2,-1,-1):
    print(i)
    if arr[i] < arr[i+1]:
        for j in range(i+1):
            ans.append(arr[j])
        print(ans)
        arr[i],arr[i+1] = arr[i+1],arr[i]
        ans1 = arr[i+1:]
        print(ans1)
        ans1.sort()
        ans+=ans1
        break
print(''.join(map(str,ans)))