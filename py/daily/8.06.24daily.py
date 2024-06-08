class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(0,len(nums)-1):
            for j in range(i,len(nums)):
                if sum(nums[i:j+1])==k:
                    return True
        return False
