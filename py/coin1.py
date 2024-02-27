from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialization: Use float('inf') instead of -1
        d = [float('inf')] * (amount + 1)
        
        # Base Case: No coins needed to make up an amount of 0
        d[0] = 0
        
        # Loop through each coin
        for coin in coins:
            # Update the 'd' list for each amount from the coin value to the target amount
            for i in range(coin, amount + 1):
                # Update 'd[i]' to be the minimum of its current value and 1 plus 'd[i - coin]'
                d[i] = min(d[i], 1 + d[i - coin])
        
        # Return the result: float('inf') if not possible, otherwise the minimum number of coins
        return d[amount] if d[amount] != float('inf') else -1

sol=Solution()
coin=[1,2,5]
k=10
print(sol.coinChange(coin,k))