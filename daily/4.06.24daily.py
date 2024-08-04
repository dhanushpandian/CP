#brute Force apporach:
class Solution:
    def longestPalindrome(self, s: str) -> int:
        m= 1
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i:j+1]==s[j:i+1:-1]:
                    m=max(abs(i-j),m)
        return m
    
#Optimized approach:
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=0
        flag_odd=False
        
        for i in d.values():
            if i%2==0:
                l+=i
            else:
                l+= i -1
                flag_odd=True
        if flag_odd:
            l+=1
        return l
    
'''
this question was asked to me in an interview and i was able to solve it partially using the brute force approach .
'''