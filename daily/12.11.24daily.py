class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ans=[]
        #items.sort()
        for i in queries:
            x=[]
            for j in items:
                if j[0] <= i:
                    x.append(j[1])
            if len(x) < 1:
                ans.append(0)
            else:
                ans.append(max(x))
        return ans
    

class Solution: 
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]: 
        items.sort() 
        d = {i: 0 for i in queries} 
        queries_sorted = sorted(queries) 
        max_beauty = 0 
        j = 0 
        for q in queries_sorted: 
            while j < len(items): 
                if items[j][0] > q:
                    break
                max_beauty = max(max_beauty, items[j][1]) 
                j += 1 
            d[q] = max_beauty 
        return [d[q] for q in queries]