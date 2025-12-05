class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        l=nums[0]
        r=sum(nums)-l
        i=0
        ans=0
        while i< len(nums)-1:
            if abs(l-r) %2==0:
                ans+=1
            l+=nums[i]
            r-=nums[i]
            i+=1
        return ans

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return len(nums)-1 if sum(nums)%2==0 else 0

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return len(nums)-1 if sum(nums)&1==0 else 0