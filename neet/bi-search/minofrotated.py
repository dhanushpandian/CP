class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        
        # If no rotation found, the minimum is the first element
        return nums[0]
    

#binery search sol

class Solution:
    def findMin(self, nums: List[int]) -> int:
        def finding(nums,left,right):
            if left == right:
                return nums[left]
            elif len(nums) == 2:
                if nums[left] < nums[right]:
                    return nums[left]
                else:
                    return nums[right]
            else:
                mid = left +(right-left) //2
                leftmin = finding(nums,left,mid)
                rightmin = finding(nums,mid+1,right)
                if leftmin < rightmin:
                    return leftmin
                else:
                    return rightmin
        return finding(nums,0,len(nums)-1)
        