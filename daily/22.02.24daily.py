class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = []  
        d = {} 
        for i in trust:
            a.append(i[0])
            if i[1] in d:
                d[i[1]] += 1
            else:
                d[i[1]] = 1

        if not d:
            return 1 if n==1 else -1

        ans = max(d, key=d.get)
        if ans not in a and d[ans] == n - 1:
            return ans
        else:
            return -1
