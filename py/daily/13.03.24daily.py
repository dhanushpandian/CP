from math import sqrt
class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1: return 1
        a=[i for i in range(1,n+1)]
        l_sum=0
        r_sum=sum(a)
        for i in a:
            r_sum-=i
            #print(i,l_sum)
            if l_sum == r_sum:
                return i
            l_sum+=i
        return -1

#using maths
class Solution:
    def pivotInteger(self, n: int) -> int:
        x=sqrt((n*(n+1))/2)
        if x%1==0:
            return int(x)
        else:
            return -1

