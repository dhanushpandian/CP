class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        
        # Iterate through possible eating speeds from 1 to the maximum pile size
        for i in range(1, max_pile + 1):
            total_hours = 0
            
            # Calculate total hours for the current eating speed
            for p in piles:
                total_hours += (p + i - 1) // i
                
            # If total hours match the time constraint, return the current eating speed
            if total_hours <= h:
                return i
        
        return max_pile  # If no eating speed meets the constraint, return the max pile size



#using binary search

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            total_hours = sum((pile + mid - 1) // mid for pile in piles)
            
            if total_hours > h:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

