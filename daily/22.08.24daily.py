class Solution:
    def findComplement(self, num: int) -> int:
        s=bin(num)
        print(type(s),s)
        ans=""
        for i in s[2:]:
            if i=='0':
                ans+="1"
            else:
                ans+="0"
        return int(ans,2)
    
class Solution:
    def findComplement(self, num: int) -> int:
        a=bin(num)
        a=a[2:]
        b="1"*len(a)
        a=int(a,2)
        b=int(b,2)
        return a^b