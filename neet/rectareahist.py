class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        m = heights[-1]
        def right(i):
            mi = heights[i]
            a = 0
            for j in range(i + 1, len(heights)):
                if mi <= heights[j]: 
                    a += mi
                else:
                    break
            return a
        
        def left(i):
            mi = heights[i]
            a = 0
            for j in range(i - 1, -1, -1):
                if mi <= heights[j]:  
                    a += mi
                else:
                    break
            return a
    
        for i in range(len(heights)):
            if heights[i] > m:
                m = heights[i]  
            t = left(i) + right(i) + heights[i]
            if t > m:
                m = t
        
        return m


#neetcode solution
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        for i,v in enumerate(heights):
            start=i
            while stack and stack[-1][1]>v:
                index,height=stack.pop()
                maxarea=max(maxarea,(i-index)*height)
                start=index
            stack.append((start,v))
        for i,h in stack:
            maxarea=max(maxarea,h*(len(heights)-i))
        return maxarea