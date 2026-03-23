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
    
# ai fixed code min dp
class Solution:
    def maxProductPath(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp_max = [[0]*n for _ in range(m)]
        dp_min = [[0]*n for _ in range(m)]

        dp_max[0][0] = dp_min[0][0] = grid[0][0]

        for j in range(1, n):
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1] * grid[0][j]

        for i in range(1, m):
            dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                candidates = [
                    dp_max[i-1][j] * val,
                    dp_min[i-1][j] * val,
                    dp_max[i][j-1] * val,
                    dp_min[i][j-1] * val
                ]
                dp_max[i][j] = max(candidates)
                dp_min[i][j] = min(candidates)

        res = dp_max[m-1][n-1]
        return res % MOD if res >= 0 else -1
