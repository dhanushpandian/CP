class Solution:
    def spiralOrder(self, matrix) :
        a=[]
        cs=0
        ce=len(matrix[0])-1
        rs=0
        re=len(matrix)-1
        while(cs<=ce and rs<=re):
            for i in range(cs,ce+1):
                a.append(matrix[rs][i])
            rs+=1
            for i in range(rs,re+1):
                a.append(matrix[i][ce])
            ce-=1            
            if rs<=re:
                for i in range(ce,cs-1,-1):
                    a.append(matrix[re][i])
                re-=1
            if cs<=ce:
                for i in range(re,rs-1,-1):
                    a.append(matrix[i][cs])
                cs+=1
        return a
    
s=Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))