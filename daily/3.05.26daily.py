class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        a=[i  for i in range(len(goal)) if goal[i]==s[0]]
        if not a:
            return False
        if len(a) < 1 :
            return False
        for i in a:
            sss=goal[i:]+goal[:i]
            if sss == s:
                return True
        return False

#cool asf methord:
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal + goal