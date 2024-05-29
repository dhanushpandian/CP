#naive:
class Solution:
    def numSteps(self, s: str) -> int:
        n=0
        x=int(s,2)
        while(x!=1):
            if x%2==0:
                x=x/2
            else:
                x=x+1
            n+=1
        return n
#optimized:
class Solution:
    def numSteps(self, s: str) -> int:
        n = 0
        while s != "1":
            if s[-1] == '0':  # if the number is even
                s = s[:-1]  # remove the last character (equivalent to dividing by 2)
            else:  # if the number is odd
                s = bin(int(s, 2) + 1)[2:]  # add 1 to the number and convert back to binary
            n += 1
        return n
