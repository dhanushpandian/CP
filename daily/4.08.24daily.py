class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        a=[]
        for i in range(n):
            for j in range(i,n):
                s=sum(nums[i:j+1])
                a.append(s)
        #a.extend(nums)
        a.sort()
        s=0
        for i in range(left-1,right):
            print(a[i])
            s+=a[i]
        return s % ( (10**9) +7)