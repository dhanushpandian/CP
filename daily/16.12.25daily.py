class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(prices):
            # print(prices[i])
            j = i + 1
            l = 0
            while j < len(prices) and prices[j-1] - prices[j] == 1:
                l += 1
                j += 1
                # print(prices[i:j])
            # print("l", l)
            L = j - i  
            ans += L * (L + 1) // 2 
            i = j
        return int(ans)