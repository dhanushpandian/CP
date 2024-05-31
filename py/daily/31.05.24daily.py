#Brute forcing in O(n) space complexity
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={i:nums.count(i) for i in nums}
        return [i for i,j in d.items() if j==1]

#list Apporach
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()
        for n in nums:
            if n in ans:
                ans.remove(n)
            else:
                ans.add(n)
        return list(ans)
    
#slightly better Aprroch 
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                del d[i]
            else:
                d[i]=1
        return list(d.keys())

#Bit Manipulation       
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        mask = xor & -xor
        a = b = 0
        for n in nums:
            if n & mask:
                a ^= n
            else:
                b ^= n
        return [a, b]