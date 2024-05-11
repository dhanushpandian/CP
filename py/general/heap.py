import heapq
heap=[2,5,6,5]
heapq.heapify(heap)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
print(heap)
heapq.heappop(heap)
print(heapq.heappop(heap))
print(heap)
heapq._heapify_max(heap)
print(heap)