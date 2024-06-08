class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(0,len(nums)-1):
            for j in range(i,len(nums)):
                if sum(nums[i:j+1])==k:
                    return True
        return False

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        # Dictionary to store the first occurrence of each mod value
        mod_map = {0: -1}  # Initialize with mod 0 at index -1 for edge cases
        running_sum = 0
        
        for i in range(len(nums)):
            running_sum += nums[i]
            if k != 0:
                running_sum %= k
            
            if running_sum in mod_map:
                # Check if the length of the subarray is at least 2
                if i - mod_map[running_sum] > 1:
                    return True
            else:
                # Store the first occurrence of the mod value
                mod_map[running_sum] = i
        
        return False
