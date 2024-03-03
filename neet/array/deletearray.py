class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = []
        for i in nums:
            if val != i:
                c.append(i)
        nums[:] = c  
        return len(c)
