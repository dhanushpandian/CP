class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        c=0
        for i in range(0,len(nums)-1):
            c+=1
            if c!=nums[i]:
                return False
        if nums[-1]!=len(nums)-1:
            return False
        return True