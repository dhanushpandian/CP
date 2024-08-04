#naive approach:
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        seen=set()
        nums.sort()
        c=0
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                j=0
                while(i+j in seen):
                    j+=1
                    c+=1
                seen.add(i+j)
        return c



#optimized approach;
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        #print(nums)
        c=0
        prev=nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= prev:
                c+=prev+1-nums[i]
                nums[i]=prev+1
            prev=nums[i]
        return c    
                
