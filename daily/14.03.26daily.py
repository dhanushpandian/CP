class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        a=[]
        ll=['a','b','c']
        def rec(x,l):
            if l == n:
                a.append(x)
                return 
            for i in ll:
                if x[-1]!= i:
                    rec(x+i,l+1)
        for i in ll:
            rec(i,1)
        print(a)
        return "" if k>len(a) else a[k-1]