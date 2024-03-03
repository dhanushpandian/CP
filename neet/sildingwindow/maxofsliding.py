#TLE (not optimized)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        for i in range(len(nums)+1-k):
            a=max(nums[i:i+k])
            ans.append(a)
        return ans

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        seen = []  # This will store the indices of elements in the current window
        ans = []   # This will store the maximum values for each window

        for i in range(n):
            # If the leftmost element in the window is outside the current window, remove it
            if seen and seen[0] == i - k:
                seen.pop(0)

            # Remove elements from the back of the queue that are smaller than the current element
            while seen and nums[seen[-1]] < nums[i]:
                seen.pop()

            # Add the current index to the queue
            seen.append(i)

            # If the window has reached size 'k', start adding maximum values to the 'ans' list
            if i >= k - 1:
                ans.append(nums[seen[0]])

        return ans
