from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums) -> int:
        d={i : nums.count(i) for i in nums}
        m=max(d.values())
        ans=0
        for i in d.values():
            if i==m: ans+=1
        return ans*m

    def maxFE(self, nums) -> int:
        d = Counter(nums)
        print(d)
        counter = 0
        for v in d.values():
            print(v)
            if v == max(d.values()):
                counter += v
        return counter
sol=Solution()
print(sol.maxFE([11,22,33,44,5]))