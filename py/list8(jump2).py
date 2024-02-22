#using Greedy algorithm, we find the max of a slot and choose the max as next move

def jump(nums) -> int:
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
    

