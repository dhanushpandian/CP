class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        c = 0
        prev_group = 0
        curr_group = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_group += 1
            else:
                # when switching, add min(prev_group, curr_group)
                c += min(prev_group, curr_group)
                prev_group = curr_group
                curr_group = 1

        # final group comparison
        c += min(prev_group, curr_group)
        return c
    

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        c = 0
        g = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                g += 1
            else:
                l = i - 1
                r = i
               
                while l >= 0 and r < len(s) and s[l] != s[r]:
                    c += 1
                    l -= 1
                    r += 1
                g = 1  
        return c
    


class Solution:
    def isValid(self,s:str):
        l=len(s)
        if l>0:
            if s[0]=='1':
                n=0
                i=0
                while i<l:
                    if s[i]=='1':
                        n+=1
                        i+=1
                    else:
                        if s[i:]=='0'*n : 
                            return True
                        else:
                            return False
            else:
                n=0
                i=0
                while i<l:
                    if s[i]=='0':
                        n+=1
                        i+=1
                    else:
                        if s[i:]=='1'*n : 
                            return True
                        else:
                            return False
                
    def countBinarySubstrings(self, s: str) -> int:
        a=[i for i in s]
        l=len(a)   
        # print(self.isValid(s))     
        c=0
        for i in range(l):
            for j in range(l):
                st=s[i:j+1]
                # print(st)
                # print(st,self.isValid(st))
                if self.isValid(st):
                    c+=1
        return c    
    

