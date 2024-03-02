#brute force approach
class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        if target in nums:
            return 1
        j=1
        while j<len(nums)+1:
            for i in range(len(nums)-1):
                s=sum(nums[i:i+j])
                if s == target:
                    return j
            j+=1
        return 0

#two pointer approach
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total=0
        res=float("inf")
        for r in range(len(nums)):
            total +=nums[r]
            while total >= target:
                res=min(r - l + 1,res)
                total -=nums[l]
                l += 1
        return res if res!=float("inf") else 0