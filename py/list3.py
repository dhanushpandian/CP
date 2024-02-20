#remove duplicates and arrage the 1st k slots and return k (no repetion)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    
# remove repetitions more than at most two times
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
            else:
                d[i]+=1
                d[i]=1
        a=[]
        for i in d.keys():
            c=0
            for j in range(d[i]):
                if c<2:
                    a.append(i)
                    c+=1
        for i,v in enumerate(a):
            nums[i]=v
        return len(a)