class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m=[[0 for i in range(n)] for i in range(n)]
        c=1
        rs=0
        re=n-1
        cs=0
        ce=n-1
        while (rs<=re and cs<=ce):
            for i in range(cs,ce+1):
                # print(m)
                m[rs][i]=c
                c+=1
            rs+=1
            for i in range(rs,re+1):
                # print(m)
                m[i][ce]=c
                c+=1
            ce-=1
            
            for i in range(ce,cs-1,-1):
                # print(c)
                m[re][i]=c
                c+=1
            re-=1
            for i in range(re,rs-1,-1):
                # print(c)
                m[i][cs]=c
                c+=1
            cs+=1
        return m


s=Solution()
print(s.generateMatrix(3))