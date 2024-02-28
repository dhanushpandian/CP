class Solution:
    def dp_rob(self, nums) -> int:
        r1 = 0
        r2 = 0
        for n in nums:
            t=max(r1 + n, r2)
            r1 = r2
            r2 = t
        return r2
    def memo_rob(self, nums) -> int:
        dp=[0]
        dp.append(nums[0])
        for i in range(1,len(nums)):
            dp.append( max( nums[i] + dp[-2] , dp[-1]) )
        print(dp)
        return dp[-1]
sol=Solution()
a=[1,2,3,4]
print(sol.dp_rob(a))
print(sol.memo_rob(a))