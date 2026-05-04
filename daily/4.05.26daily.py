class Solution:
    def rotate(self, matrix) -> None:
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
        

# how zip works:
a=[1,2,3]
b=[4,5,6]
for i,j in zip(a,b):
    print(i,j)

#solution using zip:
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])
#explaination of zip(*matrix[::-1]):
#matrix[::-1] will reverse the matrix, so the last row becomes the first row, the second last row becomes the second row, and so on.
#zip(*matrix[::-1]) will unpack the reversed matrix and zip the columns together, effectively rotating the matrix 90 degrees clockwise. The zip function takes the first element of each row and creates a new row, 
# then takes the second element of each row and creates another new row, and so on. This results in the rotated matrix.   

#why * is used in zip(*matrix[::-1]):
#The * operator is used to unpack the list of rows in the reversed matrix. When we use zip(*matrix[::-1]), it takes each row of the reversed matrix and passes it as a separate argument to the zip function.
#For example, if matrix[::-1] is [[7, 4, 1], [8, 5, 2], [9, 6, 3]], then zip(*matrix[::-1]) is equivalent to zip([7, 4, 1], [8, 5, 2], [9, 6, 3]). This allows the zip function to combine the first elements of each row into a new row, the second elements into another new row, and so on, effectively rotating the matrix.

# sample working of zip(*matrix[::-1]):
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[::-1] = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
zip(*matrix[::-1]) = zip([7, 8, 9], [4, 5, 6], [1, 2, 3]) = [(7, 4, 1), (8, 5, 2), (9, 6, 3)]