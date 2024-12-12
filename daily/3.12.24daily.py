class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        a=""
        prev=0
        for i in spaces:
            a+=s[prev:i]
            a+=" "
            prev=i
        a+=s[prev:]
        return a