class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a=sorted(heights)
        c=0
        for i in range(len(a)):
            if a[i]!=heights[i]:
                c+=1
        return c