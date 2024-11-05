class Solution:
    def minChanges(self, s: str) -> int:
        c=0
        for i in range(0,len(s)-1,2):
            #print(i,s[i],s[i+1])
            x=s[i]+s[i+1]
            if x == '01' or x == '10':
                c+=1
        return c
    
class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i]!=s[i+1] for i in range(0, len(s), 2))
        