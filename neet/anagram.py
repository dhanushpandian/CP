class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
    

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