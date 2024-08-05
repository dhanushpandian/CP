#Optimized Approach
class Solution:
    def subsum(self,arr):
        a=[]
        s=0
        for i in arr:
            s+=i
            a.append(s)
        return a
    def minSwaps(self, nums: List[int]) -> int:
        c=sum(nums)
        m=float('inf')
        l=len(nums)
        nums.extend(nums[:c])
        a=self.subsum(nums)
        for i in range(l):
            cs= a[i+c-1] if i==0 else a[i+c-1] - a[i-1]
            m=min(c-cs,m)
        return m
    
#Naive Approach
class Solution:
    def minSwaps(se1f, nums):
        c=sum(nums)
        m=float('inf')
        l=len(nums)
        nums.extend(nums[:c])
        for i in range(l):
            m=min(c-sum(nums[i:i+c]),m) 
        return m