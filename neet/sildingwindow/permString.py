from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        z=Counter(s1)
        l=len(s1)
        for i in range(0,len(s2)-l+1):
            if Counter(s2[i:i+l])==z:
                return True
        return False
        
            
#-----------------------------------------------------------

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        if(n>m):
            #Edge case
            return False
        l=[0]*26
        p=[0]*26
        #adding the characters upto the length of the first string..
        for i in range(0,n):
            l[ord(s1[i])-ord('a')]+=1
            p[ord(s2[i])-ord('a')]+=1
        if(l==p):
            return True
        #sliding window technquie just append the character and remove the characters from the starting....
        for i in range(n,m):
            p[ord(s2[i])-ord('a')]+=1
            p[ord(s2[i-n])-ord('a')]-=1
            if(l==p):
                return True
        return False

#-----------------------------------------------------------



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ordmap = [0]*26
        for i in s1:
            ordmap[ord(i) - ord('a')] += 1
        for i in range(len(s2)-len(s1)+1):
            ordmap1 = [0]*26
            for char in s2[i:i+len(s1)]:
                ordmap1[ord(char)-ord('a')] += 1
            if ordmap1 == ordmap: return True
        return False