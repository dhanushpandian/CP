#naive
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        a=0
        for i in nums:
            if i!= val:
                k+=1
                nums[a]=i
                a+=1
        return k
    
#real sneaky approach
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                # Swap with the last element
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t 
                j -= 1
            else:
                i += 1
        # The new length is the index where 'i' stopped
        return i
