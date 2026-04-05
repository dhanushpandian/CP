class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        l=len(encodedText)
        cols=int(l/rows)
        a=[[0]*cols for i in range(rows) ]
        ll=0
        for i in range(rows):
            for j in range(cols):
                a[i][j]=encodedText[ll]
                ll+=1
        # ans=""
        # # for i in range(rows):
        # #     for j in range(cols):
        # #         if a[i][j] != ' ':
        # #             ans+=a[i][j]
        # # print(ans)
        # # for i in range(rows-1,-1,-1):
        # #     for j in range(cols):
        # #         if j>rows:
        # #             break
        # #         print((i,j),a[i][j],end='')
        # for d in range(rows + cols - 1):
        #     # Each diagonal starts either in first column or last row
        #     if d < rows:
        #         i, j = d, 0
        #     else:
        #         i, j = rows - 1, d - rows + 1

        #     diagonal = []
        #     while i >= 0 and j < cols:
        #         diagonal.append(a[i][j])
        #         i -= 1
        #         j += 1

        #     # Print diagonal elements
        #     for val in diagonal:
        #         print(val, end=' ')
            # print(diagonal)
                # t= i if i != " " for i in 
        ans=[]
        for i in range(cols):
            r=0
            c=i

            while r<rows and c<cols:
                ans.append(a[r][c])
                r+=1
                c+=1
        
        return "".join(ans).rstrip()