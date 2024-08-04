class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        nums.sort()
        print(nums)
        while (r>l):
           # print(nums[r],nums[l]*-1)
            if nums[r] == nums[l]*-1:
                return nums[r]
            if nums[r] > nums[l]*-1:
                r-=1
            if nums[r] < nums[l]*-1:
                l+=1
        return -1
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] > 0 and -nums[i] in nums:
                return nums[i]
        return -1  # If no such pair found