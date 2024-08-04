class Solution:
    def sortedSquares(self, nums):
        return sorted([i**2 for i in nums])
        # nums=[i**2 for i in nums]
        # return sorted(nums)


sortedSquares = lambda nums: sorted([num**2 for num in nums])

# Example 1
nums1 = [-4, -1, 0, 3, 10]
output1 = sortedSquares(nums1)
print("Example 1:", output1)

# Example 2
nums2 = [-7, -3, 2, 3, 11]
output2 = sortedSquares(nums2)
print("Example 2:", output2)

x = [1, 2, 3, 4]
y = list(map(lambda i: i**2, x))
print(y)
