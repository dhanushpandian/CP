class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        for i in range(len(nums)-k+1):
            print(nums[i:i+k])
            prev=nums[i]
            x=nums[i+k-1]
            for j in nums[i+1:i+k]:
                if prev + 1 == j :
                    prev=j
                else:
                    x=-1
                    break
            ans.append(x)
        return ans