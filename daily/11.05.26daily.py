class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            # print(i)
            l=str(i)
            for j in l:
                a.append(int(j))
        return a