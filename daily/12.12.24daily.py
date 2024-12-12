class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        def maxidx():
            m=0
            for i in range(len(gifts)):
                if gifts[i] > gifts[m]:
                    m=i
            return m
        #print(maxidx())
        for i in range(k):
            m=maxidx()
            gifts[m]//=gifts[m]**0.5
        return int(sum(gifts))

#using heapq
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-1 * i for i in gifts]
        print(gifts)
        heapq.heapify(gifts)
        for i in range(k):
            m=heapq.heappop(gifts) * -1
            m = int( m**0.5 )
            heapq.heappush(gifts,m * -1)
        return sum(gifts)* -1