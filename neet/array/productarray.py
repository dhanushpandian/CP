from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Calculate the product of all elements to the left of each element
        left_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]
            answer[i] *= left_product
        
        # Calculate the product of all elements to the right of each element and multiply with the left product
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer
