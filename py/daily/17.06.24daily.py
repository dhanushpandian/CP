#brute force approach:
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c/2)+2):
            for j in range(int(c/2)+2):
               # print(i,j)
                if i**2 + j**2 == c:
                    return True
        return False
    
#memo approach:
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq={}
        for i in range(int(c/2)+2):
            if i not in sq:
                sq[i]=i**i
               # print(i,j)
            for j in range(int(c/2)+2):
                if j not in sq:
                    sq[j]=j*j
                if sq[i]+sq[j] == c:
                    return True
        return False

#two pointer approach:
