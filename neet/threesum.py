from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the input list in ascending order
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates for the first element in the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1  # Pointer for the second element
            right = len(nums) - 1  # Pointer for the third element
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second and third elements in the triplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers towards the center
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    # Increase the sum by moving the left pointer to a larger element
                    left += 1
                else:
                    # Decrease the sum by moving the right pointer to a smaller element
                    right -= 1
        
        return result
