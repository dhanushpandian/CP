from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                return nums1[i]
            if nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        return -1

sol=Solution()
a=[1,2,3,4,5]
b=[2,3,4]
print(sol.getCommon(a,b))