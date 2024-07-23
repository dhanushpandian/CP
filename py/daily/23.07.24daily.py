
class Solution:
    def frequencySort(self, nums):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        a = [[d[i], i] for i in d]
        a.sort()
        d2 = {}
        for i in a:
            if i[0] not in d2:
                d2[i[0]] = []
            d2[i[0]].append(i[1])
        # print(d2)
        for i in d2:
            d2[i].sort(reverse=True)
       # print(d2)
        ans = []
        for i in d2.keys():
            # print(d2[i])
            for k in d2[i]:
                for _ in range(i):
                    ans.append(k)

        return ans


s = Solution()
a = list(map(int, input().split(" ")))
# a = [2, 2, 1, 2, 3, 1, 1]
print(s.frequencySort(a))
