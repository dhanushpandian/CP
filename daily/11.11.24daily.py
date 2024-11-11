class Solution:
    def __init__(self):
        self.p = [2] 

    def isprime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime(self, n: int) -> int:
        if self.p[-1] >= n:
            for i in range(len(self.p)):
                if self.p[i] >= n:
                    return self.p[i-1]
        else:
            x = self.p[-1]
            while x < n:
                x += 1
                if self.isprime(x):
                    self.p.append(x)
            return self.p[-2] if self.p[-2] < n else self.p[-1]

    def primeSubOperation(self, nums: List[int]) -> bool:
        #if len(nums) < 2 : return True 
        prev=nums[0] 
        i=1
        while i<len(nums): 
            if nums[i] > prev: 
                prev=nums[i]
            else: 
                nums[i]-=self.prime(nums[i])
                if nums[i] < prev or nums[i] >nums[i+1]:
                    return False
            i+=1 
        return True 
