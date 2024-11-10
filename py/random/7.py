class Solution:
    def reverse(self, x: int) -> int:
        f= True if x < 0 else False
        a=0
        if f : x*=-1
        while x > 0 :
            a*=10
            a+= x%10
            x//=10
        if not -2**31 <= a <= 2**31 - 1: return 0
        return a * -1 if f else a