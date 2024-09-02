class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i=0
        n=len(chalk)
        while True:
            #print(i,chalk[i % n],k)
            if chalk[i % n] <= k:
                k-= chalk[i % n]
            else: 
                return i % n
            i+=1
#optimized
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i=0
        n=len(chalk)
        k%=sum(chalk)
        #print(s,k)
        while True:
            #print(i,chalk[i % n],k)
            if chalk[i % n] <= k:
                k-= chalk[i % n]
            else: 
                return i % n
            i+=1