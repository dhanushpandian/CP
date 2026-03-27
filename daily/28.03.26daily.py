class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        c=0
        new=[i for i in mat]

        for i in range(len(mat)):
            a=[j for j in mat[i]]
            s=k%len(a)
            if i%2!=0:
                a=a[-s:]+a[:-s]    
            else:
                a=a[s:]+a[:s]
            
            if new[i]!=a:
                return False
                
        return True
    
#optimized code
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        c=0
        new=[i for i in mat]
        s=k%len(new[0])
        for i in range(len(mat)):
            if i%2==0:
                new[i]=new[i][s:]+new[i][:s]
            else:
                new[i]=new[i][-s:]+new[i][:-s]    
            if new[i]!=mat[i]:
                return False
        return True