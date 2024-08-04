class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps={}
        mapt={}
        for i in s:
            if i not in maps:
                maps[i]=1
            else:
                maps[i]+=1
        for i in t:
            if i not in mapt:
                mapt[i]=1
            else:
                mapt[i]+=1
        a=list(maps.values())
        b=list(mapt.values())
        print(a,b)
        return a==b

s=Solution()
print(s.isIsomorphic("egg","add")) #True
print(s.isIsomorphic("foo", "bar")) # False
print(s.isIsomorphic("paper", "title")) # True



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
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
        