class Solution:
   def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    seen = {}
    for i, value in enumerate(nums):
        if nums[i] in seen:
            if (i - seen[value]) <= k:
                return True
        seen[value] = i
    return False
   
sol=Solution()
print(sol.containsNearbyDuplicate([1,2,3,2,1,3],2))