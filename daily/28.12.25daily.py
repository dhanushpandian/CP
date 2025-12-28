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