#brute force apporach
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        def func(t):
            # print(t)
            c = 0
            b = 0
            for i in t:
                if i == 0:
                    c += 1
                else:
                    b += c // k
                    c = 0
                if b >= m:
                    return True
            b += c // k
            return b >= m
        # print(func([0,0,0,1,1,1]))
        a=sorted(list(set(bloomDay)))
        for i in a:
            t=[1 if j-i > 0 else 0 for j in bloomDay]
            #print(func(t),t)
            if func(t):
                return i
        return a[-1]