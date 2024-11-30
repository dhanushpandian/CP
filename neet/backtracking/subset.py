class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res
    
    def subset2(self,nums:List[int])->List[List[int]]:
        ans=[]
        s=[]
        def dfs(i):
            if i >= len(nums):
                ans.append(s[:])
                return
            s.append(nums[i])
            dfs(i+1)
            s.pop()
            dfs(i+1)
        dfs(0)
        return ans