class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        def mul(a):
            ans=1
            for i in a:
                ans*=i
            #print(ans)
            return ans
        n=len(nums)
        c=0
        for i in range(n):
            for j in range(i,n):
                #print(i,j)
                if mul(nums[i:j+1])<k:
                    c+=1
        return c

