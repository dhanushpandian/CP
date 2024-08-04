from typing import List
#Naive solution
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        a=[]
        for i in range(n):
            for j in range(i,n):
                s=sum(nums[i:j+1])
                a.append(s)
        #a.extend(nums)
        a.sort()
        s=0
        for i in range(left-1,right):
            print(a[i])
            s+=a[i]
        return s % ( (10**9) +7)
    
nums=[1,2,3,4]
# a=[s+i for i in nums for s in a]
subarray_sums = [sum(nums[start:end]) for start in range(len(nums)) for end in range(start + 1, len(nums)+1)]
print(subarray_sums)

#One-Liner
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        return sum(sorted([sum(nums[start:end]) for start in range(len(nums)) for end in range(start + 1, len(nums)+1)])[left-1:right]) % (10**9 +7)



 #Optimized solution   
def subarrsums(arr,n):
    a=[]
    s=0
    for i in range(n):
        s+=arr[i]
        a.append(s)
        #print(s)
    ans=[]
    # ans.append(a[0])
    for i in range(n):
        for j in range(i,n):
            #print(a[i],a[j])
            if i==0:
                ans.append(a[j])
            else:
                ans.append(a[j]-a[i-1])
    return ans
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        return sum(sorted(subarrsums(nums,n))[left-1:right]) % (10**9 +7)