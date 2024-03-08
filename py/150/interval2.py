from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        output=[intervals[0]]
        for start,end in intervals[1:]:
            lastend=output[-1][1]
            if start <= lastend:
                output[-1][1]=max(lastend,end)
            else:
                output.append([start,end])
        return output
    
func=lambda a,b,c :a+b-c
print(func(1,3,2))