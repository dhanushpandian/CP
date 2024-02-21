class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        # Step 1: Initialize shift to 0
        shift = 0

        # Step 2: Use a while loop to find common prefix
        while left < right:
            # Step 3: Right-shift left and right
            left >>= 1
            right >>= 1
            
            # Step 4: Increment the shift variable
            shift += 1

        # Step 5: Left-shift left by shift positions
        return left << shift

# Sample usage for range [2, 10]
sol = Solution()
result = sol.rangeBitwiseAnd(2, 10)
print(result)  # Output: 0
