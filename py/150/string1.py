#naive approach
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        a = strs[0]
        i = 0
        c = 0
        l = len(a)
        while i < l:
            for j in strs:
                if a[i] == j[i] and len(j) >= l:
                    c += 1
                else:
                    break
            i += 1
        return a[:c]
#Co-Pilot approach
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Sort the list of strings
        strs.sort()
        
        # Take the first (smallest) string and the last (largest) string
        first_str = strs[0]
        last_str = strs[-1]
        
        i = 0
        # Find the common prefix between the first and last string
        while i < len(first_str) and i < len(last_str) and first_str[i] == last_str[i]:
            i += 1
            
        return first_str[:i]
