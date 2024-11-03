class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s)==len(goal) and goal in s+s
    
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a=s[0]
        x=goal.index(a)
        y=goal[x:]+goal[:x]
        return s==y
    
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if lengths are the same first
        if len(s) != len(goal):
            return False
        # Check if goal is a rotation of s
        return goal in s + s
