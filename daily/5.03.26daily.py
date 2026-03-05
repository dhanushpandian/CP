class Solution:
    def minOperations(self, s: str) -> int:
        a=""
        if s[0]=='1':
            for i in range(len(s)):
                if i%2==0:
                    a+='1'
                else:
                    a+='0'
        else:
            for i in range(len(s)):
                if i%2==0:
                    a+='0'
                else:
                    a+='1'
        print(s)
        print(a)
        b=""
        for i in a:
            if i=='1':
                b+='0'
            else:
                b+='1'
        print(b)
        c1=0
        c2=0
        for i in range(len(s)):
            if s[i]!=a[i]:
                c1+=1
            if s[i]!=b[i]:
                c2+=1
        return min(c1,c2)