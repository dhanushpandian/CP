class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j],end=" ")
                if grid[i][j] < 0 :
                    break
                c+=1
            print()
        return len(grid)*len(grid[0]) - c
    

# 1 2 3 4 -1 -2  -3 
# l     m         r
#       l    m    r
#       l  m  r

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in range(len(grid)):
            l=0
            r=len(grid[i])-1
            while l<=r:
                m = (r+l)//2
                if grid[i][m] < 0:
                    r = m -1
                else:
                    l = m + 1
            c+= len(grid[i]) - l
        return c
                

