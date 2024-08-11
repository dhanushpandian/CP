from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:        
        a=[]
        cs=0
        ce=cols-1
        rs=0
        re=rows-1
        while(cs<=ce and rs<=re):
            for i in range(cs,ce+1):
                a.append([rs,i])
            rs+=1
            for i in range(rs,re+1):
                a.append([i,ce])
            ce-=1            
            if rs<=re:
                for i in range(ce,cs-1,-1):
                    a.append([re,i])
                re-=1
            if cs<=ce:
                for i in range(re,rs-1,-1):
                    a.append([i,cs])
                cs+=1
        return a
    
s=Solution()
print(s.spiralMatrixIII(5,6,1,4))
