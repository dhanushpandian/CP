class Solution:
    def searchRange(self, nums, target: int) :
        ans=[]
        c=0
        if target not in nums:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
            elif nums[i] > target:
                # ans.append(i-1)
                break
        # print(ans)
        # print(len(ans))
        # if len(ans) == 2:
        return [ans[0],ans[-1]]
        # else:
        # return [-1,-1]