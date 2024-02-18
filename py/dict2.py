class Solution:
    def iisIsomorphic(self, s: str, t: str) -> bool:
        map1=[]
        map2=[]
        for i in s:
            map1.append(s.index(i))
        for i in t:
            map2.append(t.index(i))
        print(map1,map2,sep='\n')
        if map1==map2:
            return True
        return False
 
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        for i in range(len(s)):
            if s[i] not in map_s:
                map_s[s[i]] = t[i]

            if t[i] not in map_t:
                map_t[t[i]] = s[i]

            if map_t[t[i]] != s[i] or map_s[s[i]] != t[i]:
                print(map_s,map_t,sep='\n')
                return False
        print(map_s,map_t,sep='\n')
        return True

sol=Solution()    
print(sol.iisIsomorphic("aa","bb"))
print(sol.isIsomorphic("aa","bb"))





