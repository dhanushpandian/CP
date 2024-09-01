class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original): return []
        k=0
        ans=[]
        for i in range(m):
            ans.append([])
            for j in range(n):
                #print(i,j)
                ans[i].append(original[k])
                k+=1
        return ans 

#using  list comprehension
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [] if len(original)!=m*n else [original[n*i:(i+1)*n] for i in range(m)]
        #[original[i*n : (i+1)*n] for i in range(m)]