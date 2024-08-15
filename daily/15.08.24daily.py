class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d={5:0,10:0}
        for i in bills:
            if i==5:
                d[5]+=1
            elif i==10:
                d[10]+=1
                d[5]-=1
            else:
                if d[10] > 0:
                    d[10]-=1
                    d[5]-=1
                else:
                    d[5]-=3
            x=list(d.values())
            for i in x:
                if i < 0:
                    return False
        # x=list(d.values())
        # for i in x:
        #     if i < 0:
        #         return False
        return True