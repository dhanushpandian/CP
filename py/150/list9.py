class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        for i, v in enumerate(citations,1):
            if v >= i:
                ans = i
        return ans
