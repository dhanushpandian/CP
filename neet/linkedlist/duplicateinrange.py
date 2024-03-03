def findDuplicate(self, nums) -> int:
    d={}
    for i in nums:
        if i in d:
            return i
        else:
            d[i]=1

#using linkedlist floyds algo
def findDuplicate2(self, nums: List[int]) -> int:
    slow=nums[0]
    fast=nums[0]
    while(True):
        slow=nums[slow]
        fast=nums[nums[fast]]
        if slow==fast:
            break
    slow2=nums[0]
    while slow!=slow2:
        slow=nums[slow]
        slow2=nums[slow2]
    return slow2