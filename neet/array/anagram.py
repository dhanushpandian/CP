from collections import Counter

# ! Sorting
def isAnagram(a,b):
    return sorted(a) == sorted(b)

# ! HashMaps
def isAnagram(a,b):
    if(len(a) != len(b)):return False
    mapA,mapB = {},{}
    for i in range(len(a)):
        mapA[a[i]] = 1 + mapA.get(a[i],0)
        mapB[b[i]] = 1 + mapB.get(b[i],0)
    return mapA == mapB    

# ! Counter
def isAnagram(a,b):
    return Counter(a) == Counter(b)
    

class Solution(object):
    def isAnagram(self, s, t):
        if(len(s)==len(t)):
            for i in s:
                if i in t:
                    t=t.replace(i,"",1)
                else:
                    return False
            return True
        else:
            return False