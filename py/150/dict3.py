class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            print(n)
            seen.add(n)
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            n = s
        return n == 1
sol=Solution()
print(sol.isHappy(124))