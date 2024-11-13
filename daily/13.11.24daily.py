class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        c=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                #print(i,j)
                if 0 <= i and i < j and j < len(nums) and lower <= nums[i] + nums[j] and nums[i] + nums[j]<= upper:
                    c+=1
        return c

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        c=0
        nums=sorted(list(set(nums)))
        print(nums)
        l=len(nums)
        i=0
        j=1
        while i<j and 0<=i and j<l:
            s=nums[i]+nums[j]
            print(i,j,s)
            if s>=lower and s<=upper:
                c+=1
                j+=1
            elif s > upper:
                i+=1
                j=i+1
            else:
                i+=1
                j+=1
        return c
