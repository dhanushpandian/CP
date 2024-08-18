class Solution:
    def isUgly(self, n: int) -> bool:
        if n <=0 :
            return False
        a=[2,3,5]
        for i in a :
            while(n%i==0):
                n//=i
        return n==1 or n==0


class Solution:
    def isprime(x):
        if x==1 or x==0:
            return False
        else:
            for i in range(2,int(x**0.5)):
                if x%i==0:
                    return False
        return True
    def ugly(n):
        p=[]
        for i in range(n):
            if Solution.isprime(i) and n%i==0:
                p.append(i)
        p=set(p)
        a=set([2,3,5])
        print(p,a)
        print(p.difference(a))
        return list(p - a)

    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        x=Solution.ugly(n)
        return True if len(x)==0 else False

    


