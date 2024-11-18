class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        c=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                #print(i,j)
                if 0 <= i and i < j and j < len(nums) and lower <= nums[i] + nums[j] and nums[i] + nums[j]<= upper:
                    c+=1
        return c

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        c=0
        nums=sorted(list(set(nums)))
        print(nums)
        l=len(nums)
        i=0
        j=1
        while i<j and 0<=i and j<l:
            s=nums[i]+nums[j]
            print(i,j,s)
            if s>=lower and s<=upper:
                c+=1
                j+=1
            elif s > upper:
                i+=1
                j=i+1
            else:
                i+=1
                j+=1
        return c

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()  
        c = 0 
        for i in range(len(nums)):
            left = self.find_left(nums, i+1, lower - nums[i])
            right = self.find_right(nums, i+1, upper - nums[i])
            c += right - left
        return c
    
    def find_left(self, nums: List[int], start: int, target: int) -> int:
        low, high = start, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

    def find_right(self, nums: List[int], start: int, target: int) -> int:
        low, high = start, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return low

'''

1. **Main function: `countFairPairs`**
   - The function takes three parameters: `nums` (the list of integers), `lower` (the lower bound of the range), and `upper` (the upper bound of the range).
   - The first step is to sort the `nums` list in ascending order.
   - We initialize a variable `c` to keep track of the total count of fair pairs.
   - Then, we iterate through the `nums` list using a for loop, starting from index 0.
   - For each element `nums[i]`, we call the `find_left` and `find_right` helper functions to find the left and right indices of the range of elements that, when added to `nums[i]`, fall within the `[lower, upper]` range.
   - We then calculate the difference between the right and left indices, which gives us the count of fair pairs for the current `nums[i]`.
   - We add this count to the overall `c` variable.
   - Finally, we return the total count `c`.

2. **Helper function: `find_left`**
   - This function takes three parameters: `nums` (the sorted list of integers), `start` (the starting index to search from), and `target` (the target value to find the left boundary for).
   - The function uses a binary search approach to find the leftmost index of the range of elements that are greater than or equal to the `target` value.
   - It initializes `low` to the `start` index and `high` to the length of the `nums` list.
   - In each iteration of the while loop, it calculates the `mid` index as the average of `low` and `high`.
   - If the element at the `mid` index is less than the `target`, the function updates `low` to `mid + 1`, as the left boundary must be to the right of the current `mid` index.
   - If the element at the `mid` index is greater than or equal to the `target`, the function updates `high` to `mid`, as the left boundary might be at the current `mid` index or to the left of it.
   - The loop continues until `low` is no longer less than `high`, at which point the function returns the `low` index, which is the leftmost index of the range of elements greater than or equal to the `target`.

3. **Helper function: `find_right`**
   - This function is similar to the `find_left` function, but it searches for the rightmost index of the range of elements that are less than or equal to the `target` value.
   - The main difference is that in the while loop, if the element at the `mid` index is less than or equal to the `target`, the function updates `low` to `mid + 1`, as the right boundary must be to the right of the current `mid` index.
   - If the element at the `mid` index is greater than the `target`, the function updates `high` to `mid`, as the right boundary might be at the current `mid` index or to the left of it.
   - The function returns the `low` index, which is the rightmost index of the range of elements less than or equal to the `target`.

This solution has a time complexity of O(n log n) due to the binary search operations, and a space complexity of O(1) since it only uses a constant amount of extra space.'''
