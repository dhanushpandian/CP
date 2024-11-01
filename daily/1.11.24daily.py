class Solution:
    def makeFancyString(self, s: str) -> str:
        ans=""
        prev=None
        c=0
        for i in s:
            if prev != i:
                ans+=i
                c=1
                prev=i
            else:
                if c < 2:
                    ans+=i
                    c+=1
        return ans
