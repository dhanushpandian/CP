class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax,rmax = [0]*n,[0]*n

        lmax[0] = height[0]
        for i in range(1,len(height)):
            lmax[i] = max(lmax[i-1],height[i])

        rmax[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            rmax[i] = max(rmax[i+1],height[i])

        ans = 0
        for i in range(n):
            ans+=min(lmax[i],rmax[i])-height[i]
        return ans