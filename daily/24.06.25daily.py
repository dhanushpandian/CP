class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        a=[]
        for i in range(len(nums)):
            if nums[i]==key:
                a.append(i)
        # print(a)
        ans={}
        for i in a:
            for j in range(len(nums)):
                # print(i,j)
                if abs(i-j) <= k:
                    if j not in ans:
                        ans[j]=0
        print(ans)
        return sorted(ans.keys())