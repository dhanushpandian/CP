class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        c = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                a = nums[i:j+1]
                flag = True
                for k in range(len(a)):
                    for l in range(k+1, len(a)):
                        if abs(a[k] - a[l]) > 2:
                            flag = False
                            break
                    if not flag:
                        break
                c += 1 if flag else 0
        return c
