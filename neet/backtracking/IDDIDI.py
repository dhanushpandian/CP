class Solution:
    def smallestNumber(self, pattern: str) -> str:
        a=[]
        ans=""
        n=1
        s=""
        for i in pattern:
            a.append(n)
            n+=1
            if i == "I":
                s += ''.join(str(i) for i in a)
                print(s)
                ans+=s[::-1]
                a=[]
                s=""
        a.append(n)
        s += ''.join(str(i) for i in a)
        print(s)
        ans+=s[::-1]
        a=[]
        return ans
        
