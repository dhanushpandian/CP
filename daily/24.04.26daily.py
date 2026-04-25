class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        d={'L':0,'R':0,'_':0}
        for i in moves:
            if i in d:
                d[i]+=1
        # print(d)
        (x,y)= (d['L'],d['R']) if d['L'] > d['R'] else (d['R'],d['L'])
        # print(x,y)
        return x+d['_']-y