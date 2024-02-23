#using Greedy algorithm, we find the max of a slot and choose the max as next move

def jumps(nums) -> int:
    ans=0
    l=0
    r=0
    while r < len(nums)-1:
        m=0
        for i in range(l,r+1):
            m=max(m,nums[i]+i)
        l=r+1
        r=m
        ans+=1
    return ans
    
# Using GPT trying out  DYnamic Proggramming approach, where array memozise the max jump to reach particular index
def jump(nums):
    n = len(nums)
    
    # Create an array to store the minimum number of jumps needed to reach each index
    jumps = [float('inf')] * n
    
    # Base case: No jumps needed to reach the starting index
    jumps[0] = 0
    
    # Iterate through the array to update the minimum jumps for each index
    for i in range(1, n):
        for j in range(i):
            # If it's possible to reach index i from index j
            if j + nums[j] >= i:
                # Update the minimum jumps needed for index i
                jumps[i] = min(jumps[i], jumps[j] + 1)
    
    return jumps[-1]

# Example usage:
nums1 = [2, 3, 1, 1, 4]
nums2 = [2, 3, 0, 1, 4]

output1 = jump(nums1)
output2 = jump(nums2)

print(output1)  # Output: 2
print(output2)  # Output: 2
