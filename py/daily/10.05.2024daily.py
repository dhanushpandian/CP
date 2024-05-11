import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []  # Heap to store the k smallest fractions
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                # Calculate the fraction and store it as negative for min-heap
                heapq.heappush(heap, (-arr[i] / arr[j], arr[i], arr[j]))
                # If heap size exceeds k, pop the smallest fraction
                if len(heap) > k:
                    heapq.heappop(heap)
        
        # Pop the kth smallest fraction from the heap
        result = heapq.heappop(heap)
        
        return [result[1], result[2]]  # Return the numerator and denominator of the fraction
