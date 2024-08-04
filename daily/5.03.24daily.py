class Solution:
    def minimumLength(self, s: str) -> int:
        a=[i for i in s]
        while len(a)>1:
            if a[0]==a[-1]:
                a.pop(0)
                a.pop(-1)
            else:
                break
        return len(a)
    
class Solution:
    def minimumLength(self, s: str) -> int:
        a=[i for i in s]
        l=""
        while len(a)>1:
            if a[0]==a[-1]:
                l=a[0]
                a.pop(0)
                a.pop(-1)
            else:
                if a[0]==l:
                    a.pop(0)
                elif a[-1]==l:
                    a.pop(-1)
                else:
                    break
        if len(a)>0 and a[0]==l:
            a.pop(0)
        return len(a)
    
sol=Solution()
s="bcdcba"
print(sol.minimumLength(s))
