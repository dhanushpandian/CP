class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d={i:arr1.count(i) for i in arr1}
        print(d)
        ans1=[]
        ans2=[]
        for i in arr2:
            for k in range(d[i]):
                ans1.append(i)
        for i in arr1:
            if i not in arr2:
                ans2.append(i)
        ans2.sort()
        print(ans1,ans2)
        ans=ans1+ans2
        return ans