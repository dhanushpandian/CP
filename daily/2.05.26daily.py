#tried DP and failed epic
class Solution:
    def rotatedDigits(self, n: int) -> int:
        r=set(['0','1','8','2','5','6','9'])
        d=set()
        # print(r,d)
        def fun(s):
            # print(s)
            if s in d or not s:
                return True
            a=s[0]
            b=s[1:]
            # print(a,b)
            if a in r and fun(b):
                d.add(s)
                return True
            return False
        c=0
        for i in range(1,n+1):
            print(i,c)
            c+= 1 if fun(str(i)) else 0
        return n-c+1


#brute force shit , actully worked
class Solution:
    def rotatedDigits(self, n: int) -> int:
        rot={'0':'0','1':'1','8':'8','2':'5','5':'2','6':'9','9':'6'}
        def fun(s):
            s1=""
            for i in s:
                if i in rot:
                    s1+=rot[i]
                else:
                    return False
            print(s,s1)
            if s1!=s:
                return True
            return False
        c=0
        for i in range(1,n+1):
            if fun(str(i)):
                c+=1
        return c

