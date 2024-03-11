class Solution:
    def customSortString(self, order: str, s: str) -> str:
        a=""
        b=""
        for i in s:
            if i not in order:
                a+=i
            else: b+=i
        b=list(b)
        for i in range(len(b)):
            for j in range(len(b)-i-1):
                if order.find(b[j]) > order.find(b[j+1]):
                    t=b[j]
                    b[j]=b[j+1]
                    b[j+1]=t
        return  "".join(b)+a

    def cSS(self, order: str, s: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            
        ans = ""
        for i in order:
            x = d.get(i, 0)
            ans += i * x

        for i in s:
            if i not in order:
                ans += i

        return ans
