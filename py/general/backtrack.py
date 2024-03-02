def generate_subsets(nums):
    def backtrack(start, path):
        subsets.append(path[:])  # Add a copy of the current subset to the result

        for i in range(start, len(nums)):
            path.append(nums[i])  # Include the current element
            backtrack(i + 1, path)  # Recur for the next index
            path.pop()  # Backtrack: remove the current element

    subsets = []
    backtrack(0, [])
    return subsets

# Example usage:
nums = [1, 2, 3]
result = generate_subsets(nums)
print(result)
