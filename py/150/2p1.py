class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return len(s) == i

sol=Solution()
text="abcedhijkdoksp"
sub="ajp"
print(sol.isSubsequence(sub,text))