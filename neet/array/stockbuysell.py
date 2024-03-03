class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0

        for right in range(len(prices)):
            if prices[right] <= prices[left]:
                left = right
            max_profit = max(max_profit, prices[right] - prices[left])
        
        return max_profit

#leetcode forum solution
def maxProfit(prices: List[int]) -> int:
    maxP = 0
    minP = prices[0]
    for price in prices[1:]:
        maxP = max(maxP, price - minP)
        minP = min(minP, price)
        
    return maxP


with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f'{str(maxProfit(case))}\n')
exit()