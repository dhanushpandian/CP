class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        maxheap=[]
        heapq.heapify(maxheap)
        # seen=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                x=abs(nums[i]-nums[j])
                # print(x)
                # if x not in seen:
                heapq.heappush(maxheap,x*-1)
                #print(maxheap,x)
                if len(maxheap) > k:
                    heapq.heappop(maxheap)
        return heapq.heappop(maxheap)*-1

