class Solution:
    def reverse1(self, s: str) -> str:
        a=list(s.split())
        print(a)
        s=""
        for i in range(len(a)-1,-1,-1):
            s+=a[i]
            s+=" "
        return s.strip()
    

    def reverse2(self, s: str) -> str:
        s = s.split()
        s = list(s)
        s = reversed(s)
        return ' '.join(s)
        