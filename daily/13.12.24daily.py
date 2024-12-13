import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        a=[[nums[i],i] for i in range(len(nums))]
        heapq.heapify(a)
        seen=set()
        score=0
        
        while(a):
            x=heapq.heappop(a)
            if x[1] not in seen:
                score+=x[0]
                seen.add(x[1])
                seen.add(1+x[1])
                seen.add(x[1]-1)

        return score
