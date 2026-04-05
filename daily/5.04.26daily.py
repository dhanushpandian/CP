class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d={i:0 for i in 'RLUD'}
        for i in moves:
            d[i]+=1
        # print(d)
        return d['R']==d['L'] and d['U']==d['D']