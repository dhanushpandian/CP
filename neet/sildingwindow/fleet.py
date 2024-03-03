
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        for p, s in sorted(zip(position, speed), reverse=True):
            reach = (target - p) / s 
            if not fleets: 
                fleets.append(reach)
            elif reach > fleets[-1]:
                fleets.append(reach)
            
        return len(fleets)  
