class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        for i in range(len(prices)):
           # print(prices[i])
            flag=True
            for j in range(i+1,len(prices)):
              #  print(i,j)
                if prices[i] >= prices[j]:
                    ans.append(prices[i]-prices[j])
                    flag=False
                    break
            if flag:
                ans.append(prices[i])
        return ans 
                    