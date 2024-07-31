#longest increasing subsequence
def lis(arr):
    l=[1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[i]>arr[j] and l[i]<l[j]+1:
                l[i]=l[j]+1
    return max(l)

def lis2(arr):
    l=[1]*len(arr)
    for i in range(1,len(arr)):
        subproblems = [l[k] for k in range(i) if arr[k]<arr[i]]
        l[i] = 1 + max(subproblems) if subproblems else 1
    return max(l)

a=[5,2,8,6,3,6,9,7]
print(lis2(a))

