class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        a=0
        l=len(strs)
        le=len(strs[0])
        for i in range(le):
            t=True
            for j in range(1,l):
                if ord(strs[j-1][i]) <= ord(strs[j][i]):
                    continue
                else:
                    t=False
                    break
            a+=1 if not t else 0
        return a