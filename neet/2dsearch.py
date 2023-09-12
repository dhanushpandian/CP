
 class Solution:
    def search(self,nums: List[int], target: int):
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
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                result = self.search(matrix[i], target)
                if result != -1:
                    return True
        return False