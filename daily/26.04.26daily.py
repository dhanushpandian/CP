# class Solution:
#     def containsCycle(self, grid: List[List[str]]) -> bool:
#         def iscycle(x,y,c,s):
#             if (x,y) in s:
#                 return True 
#             s.add((x,y))
#             if y+1<len(grid) and grid[x][y+1]==c:
#                 iscycle(x,y+1,c,s)
#             if x+1<len(grid[0]) and grid[x+1][y]==c:
#                 iscycle(x+1,y,c,s)
#             if y-1 >= 0 and grid[x][y-1]==c:
#                 iscycle(x,y-1,c,s)
#             if x-1 >= 0 and grid[x-1][y]==c:
#                 iscycle(x-1,y,c,s)
#             return False
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 s=set() 
#                 if iscycle(i,j,grid[i][j],s):
#                     return True
#         return False

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def iscycle(x, y, c, s, px, py):
            if (x, y) in s:
                return True 
            s.add((x, y))
            if y+1 < len(grid[0]) and grid[x][y+1] == c:
                if (x, y+1) != (px, py) and iscycle(x, y+1, c, s, x, y):
                    return True
            if x+1 < len(grid) and grid[x+1][y] == c:
                if (x+1, y) != (px, py) and iscycle(x+1, y, c, s, x, y):
                    return True
            if y-1 >= 0 and grid[x][y-1] == c:
                if (x, y-1) != (px, py) and iscycle(x, y-1, c, s, x, y):
                    return True
            if x-1 >= 0 and grid[x-1][y] == c:
                if (x-1, y) != (px, py) and iscycle(x-1, y, c, s, x, y):
                    return True

            return False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                s = set() 
                if iscycle(i, j, grid[i][j], s, -1, -1):
                    return True
        return False
