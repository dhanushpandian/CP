#using hash
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        cursum=0
        presum={0:1}
        for n in nums:
            cursum+=n
            dif=cursum-k
            res+=presum.get(dif,0)
            presum[cursum]=1+presum.get(cursum,0)
        return res

import collections  
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = collections.defaultdict(int)
        prefix_sums[0] = 1
        prefix_sum = 0
        res = 0
        for i in range(n):
            prefix_sum += nums[i]
            key = prefix_sum-k
            if prefix_sums[key]:
                res += prefix_sums[key]
            prefix_sums[prefix_sum] += 1
        return res

#brute force:
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                print(s)
                s+=nums[j]
                if s==k: c+=1
        return c        