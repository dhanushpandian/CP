class Solution:
    def findMin(self, nums: List[int]) -> int:
        #return min(nums)
        m=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                m=i
                break
        return nums[m]