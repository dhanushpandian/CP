from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s=0

        def xor(a: List[int]):
            s=a[0]
            for i in range(1,len(a)):
                s=s^a[i]
            return s
        
        for r in range(1, len(nums) + 1):
            for subset in combinations(nums, r):
                s += xor(list(subset))

        return s
