class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # a=12
        # print(bin(a).count('1'))
        d={i : bin(i).count('1') for i in nums}
        b=sorted(nums)
        n=len(nums)
        if nums==b: return True
        #print(b)
        flag=True
        for i in range(len(b)):
            idx=nums.index(b[i])
            if  flag:
                if idx > 0 and d.get(nums[idx-1])==d.get(nums[idx]) :
                    continue
                if idx < n-1 and d.get(nums[idx+1])==d.get(nums[idx]):
                    continue
                else:
                    flag=False
        return flag
    


