#brute force approach:
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c/2)+2):
            for j in range(int(c/2)+2):
               # print(i,j)
                if i**2 + j**2 == c:
                    return True
        return False

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # d=set()

        def is_perfect_square(num):
            sqrt_num = int(num**0.5)
            return sqrt_num * sqrt_num == num

        for i in range(int(c**0.5)+1):
            x = c - i*i
            if is_perfect_square(x):
                return True    
            # d.add(x)
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
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r=int(sqrt(c))
        l=0
        while l <= r  :
            x =  l**2 + r**2 
            if  x == c :
                return True
            elif x > c:
                r-=1
            else :
                l+=1
        return False