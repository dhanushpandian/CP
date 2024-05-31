#Brute forcing in O(n) space complexity
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={i:nums.count(i) for i in nums}
        return [i for i,j in d.items() if j==1]
    