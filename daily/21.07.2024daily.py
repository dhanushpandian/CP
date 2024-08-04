class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        a=[]
        b=[]
        for i in range(m):
            a.append(min(matrix[i]))

        for col in range(n):
            ma = 0
            for row in range(m):
                ma=max(ma,matrix[row][col])
            b.append(ma)
        print(a,b)
        
        return list(set(a).intersection(b))
    


    