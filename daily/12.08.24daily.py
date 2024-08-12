#naive approach
class KthLargest:
    def __init__(self, k: int, x: List[int]):
       self.k=k
       self.x=sorted(x) 
    def add(self, val: int) -> int:
        for i in range(len(self.x)):
            if val < self.x[i]:
                self.x.insert(i,val)
                return self.x[-self.k]
        self.x.append(val)
        return self.x[-self.k]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#heap approach
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap ,self.k = nums,k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

