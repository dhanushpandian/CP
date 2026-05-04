class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        b=len(matrix)
        l=len(matrix[0])
        for i in range(int(l)):
            for j in range(i+1,int(b)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(l):
            # print(matrix[i])
            matrix[i]=matrix[i][::-1]
            # print(matrix[i])
        