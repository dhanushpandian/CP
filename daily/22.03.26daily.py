class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat==target :
            return True
        def rotate(m):
            rows, cols = len(m), len(m[0])
            a = [[0] * rows for _ in range(cols)]  
            for i in range(rows):
                for j in range(cols):
                    a[j][rows - 1 - i] = m[i][j]
            return a
        x=rotate(mat)
        # print(x)
        y=rotate(x)
        z=rotate(y)
        a=[x,y,z]
        return True if target in a else False

