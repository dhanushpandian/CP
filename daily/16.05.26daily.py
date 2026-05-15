class Solution:
    def findMin(self, nums: List[int]) -> int:
        #return min(nums)
        m=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                m=i
                break
        return nums[m]
    
#biserachj
class Solution:
    def findMin(self, nums: List[int]) -> int:
        r=len(nums)-1
        l=0
        while r>l:
            m=(l+r)//2
            if m<len(nums) and r<len(nums) and nums[m] > nums[r]:
                l=m+1
            else:
                r=m
        return nums[l]