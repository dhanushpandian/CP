class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        total_length = n1 + n2
        is_even = total_length % 2 == 0
        
        merged = []
        i = 0
        j = 0
        
        while i < n1 and j < n2 and len(merged) <= total_length // 2:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Handle cases where one array is exhausted
        while i < n1 and len(merged) <= total_length // 2:
            merged.append(nums1[i])
            i += 1
        
        while j < n2 and len(merged) <= total_length // 2:
            merged.append(nums2[j])
            j += 1
        
        if is_even:
            median = (merged[-1] + merged[-2]) / 2
        else:
            median = merged[-1]
        
        return median
