from typing import List

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

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        return sum(sorted([sum(nums[start:end]) for start in range(len(nums)) for end in range(start + 1, len(nums)+1)])[left-1:right]) % (10**9 +7)