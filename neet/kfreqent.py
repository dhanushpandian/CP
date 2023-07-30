class Solution(object):
    def topKFrequent(self, nums, k):
        a=[]
        d={}
        for i in  nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        while(k>0):
            m = max(d, key=d.get)
            a.append(m)
            del d[m]
            k-=1
        return a

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num=Counter(nums)
        return sorted(num, key = num.get, reverse=True)[:k]