class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        a=[]
        def dp(x,y,p):
            if x>=len(grid) or y>=len(grid[0]):
                return
            p = p*grid[x][y]
            if x==len(grid)-1 and y==len(grid[0])-1:
                a.append(p)
                return
            dp(x+1,y,p)
            dp(x,y+1,p)

        dp(0,0,1)
        # print(a)
        b=[i for i in a if i >= 0 ]
        ans= max(b)  if len(b) > 0 and max(b) >= 0 else -1
        return ans % 10**9 +7 if ans>10**9 else ans