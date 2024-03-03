class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        while left <= right:
            mid = (left + right)//2
        
            if nums[mid] == target:
                return mid
        
            elif nums[mid] > target:
                right = mid - 1
        
            else:
                left = mid + 1
        
        return -1