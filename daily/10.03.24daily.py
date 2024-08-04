from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set(nums1)
        b=set(nums2)
        c=[]
        for i in a:
            if i in b:
                c.append(i)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set(nums1)
        b=set(nums2)
        c=[i for i in a if i in b]
        return c
    
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [i for i in set(nums1) if i in set(nums2)]
        
        
        