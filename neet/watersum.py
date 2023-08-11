class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                l=j-i
                b=min(height[i],height[j])
                area=l*b
                print(area)
                if area>a:
                    a=area                
        return a


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        area=min(height[i],height[j])*(j-i)
        while(i<j):
            a=min(height[i],height[j])*(j-i)
            area = a if a>area else area
            if height[i]>height[j]:
                j-=1
            elif height[i]<height[j]:
                i+=1
            else:
                if height[i+1]>height[j-1]:
                    i+=1
                else:
                    j-=1
        return area


