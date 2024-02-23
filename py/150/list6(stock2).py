class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        p=0
        for i in range(len(prices)-1):
            if prices[i]<=prices[i+1]:
                p+=prices[i+1]-prices[i]
        return p
            
def maxProfit2(prices: List[int]) -> int:
    maxP = 0
    minP = prices[0]
    for price in prices[1:]:
        maxP = max(maxP, price - minP)
        minP = min(minP, price)
        
    return maxP


