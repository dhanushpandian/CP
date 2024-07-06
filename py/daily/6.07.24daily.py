class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        d = 1
        
        while time > 0:
            if i == n:
                d = -1
            elif i == 1:
                d = 1
            
            i += d
            time -= 1
        
        return i
                    
        # x=time//n
        # d=time%n
        # print(x,d)
        # if x%2!=0:
        #     return n-d
        # else:
        #     return d
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = 2 * (n - 1)
        time_in_cycle = time % cycle_length
        
        if time_in_cycle < n:
            return time_in_cycle + 1
        else:
            return n - (time_in_cycle - (n - 1))
