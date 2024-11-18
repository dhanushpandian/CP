'''     
Betteer solution using on loop and running sum   
        if k > 0 :
            s=sum(code[i+1 % n : i+k+1 %n])
            for i in range(n):
                ans[i]=s
                s -= code[(i + 1) % n] 
                s += code[(i + k + 1) % n]
'''


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        ans=[0 for i in range(n)]
        if k > 0 :
            for i in range(n):
                s=0
                for j in range(i+1,i+k+1):
                    x=j%n
                    s+=code[x]
                ans[i]=s
        elif k == 0: return ans
        else:
            for i in range(n):
                s=0
                #print(i,code[i])
                for j in range(i+k,i):
                    x=j%n
                    #print(j,code[x])
                    s+=code[x]
                ans[i]=s
        return ans
            