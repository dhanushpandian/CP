class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        c=0
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]==1:
                c+=1
                if c==k:
                    return i
        return ""