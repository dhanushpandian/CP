class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans=0
        a=[nums[0]]
        s=sum(nums)-nums[0]
        for i in range(1,len(nums)):
            # print(a,s,ans)
            if a[i-1] >= s:
                ans+=1
            a.append(a[i-1]+nums[i])
            s-=nums[i]
        return ans
    
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pre=[nums[0]]
        for i in range(1,len(nums)):
            pre.append(pre[i-1]+nums[i])
        # print(pre)
        ans=0
        # s=sum(nums)
        for i in pre[:-1]:
            if pre[-1] - i <= i:
                ans+=1
        return ans