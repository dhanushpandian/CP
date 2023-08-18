class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        while(i<= len(haystack)-len(needle)):
            x=haystack[i:i+len(needle):]
            if x==needle:
                return i
            i+=1
        return -1
            