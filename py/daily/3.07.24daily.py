class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<5:
            return 0
        nums.sort(reverse=True)
        a=[nums[-1]-nums[3],nums[-2]-nums[2],nums[-3]-nums[1],nums[-4]-nums[0]]
        return max(a)*-1
    