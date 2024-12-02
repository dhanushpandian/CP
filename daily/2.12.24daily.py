class Solution:
    def isPrefixOfWord(self, s: str, w: str) -> int:
        i,j,c=0,0,0
        while i<len(s):
            print(i,s[i],j,w[j])
            if s[i]==w[j]:
                i+=1
                j+=1    
                if j==len(w): 
                    return c+1
            else:
                j=0
                while s[i]!=" " and i<len(s):
                    if i == len(s)-1: break
                    i+=1
                c+=1
                i+=1
        return -1
        
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a=sentence.split(' ')
        
        for i in a:
            if searchWord in i and i.index(searchWord)==0 :
                return a.index(i) + 1
        return -1