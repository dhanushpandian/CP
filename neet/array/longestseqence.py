class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        c=1
        a=[1]
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                c+=1
            elif nums[i+1]-nums[i]==0:
                continue
            else:
                c=1
            a.append(c)
        return max(a)

    def lc(self, nums: list[int]) -> int:
        # Create a set for faster membership checks
        numSet = set(nums)
        # Initialize the variable to store the longest consecutive sequence length
        longest = 0

        # Iterate through each number in the input list
        for n in nums:
            # Check if it's the potential start of a sequence
            if (n - 1) not in numSet:
                # Initialize the length of the current consecutive sequence
                length = 1
                # Expand the sequence to the right
                while (n + length) in numSet:
                    length += 1
                # Update the longest consecutive sequence length
                longest = max(length, longest)

        # Return the longest consecutive sequence length
        return longest

if __name__=='__main__':
    sol=Solution()
    a=[1,2,3,4,100,200,300]
    print(sol.lc(a))