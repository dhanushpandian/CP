class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {i: nums.count(i) for i in nums}
        return [i for i,v in d.items() if v>1 ]


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=[]
        for i,v in d.items():
            print(i,v)
            if v>1:
                ans.append(i)
        return ans