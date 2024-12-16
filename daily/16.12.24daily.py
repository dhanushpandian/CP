class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        def minn():
            m=nums[0]
            mi=0
            for i in range(1,len(nums)):
                if nums[i] < m:
                    m=nums[i]
                    mi=i
            return mi
        while k > 0:
            m=minn()
            nums[m]=nums[m]*multiplier
            #print(nums)
            k-=1
        return nums
    
#using heapq
import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        a=[[nums[i],i] for i in range(len(nums))]
        heapq.heapify(a)
        while k > 0:
            m=heapq.heappop(a)
            heapq.heappush(a,[m[0]*multiplier,m[1]])
            k-=1
        for i in a:
            nums[i[1]]=i[0]
        return nums