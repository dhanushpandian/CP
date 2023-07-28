class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
        return ans

class Solution(object):
    def twoSum(self, nums, target):
        prev={}
        for i , n in enumerate(nums):
            diff=target-n
            if diff in prev:
                return [prev[diff],i]
            prev[n]=i
