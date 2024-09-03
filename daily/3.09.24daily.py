class Solution:
    def getLucky(self, s: str, k: int) -> int:
        #val=s[i]-96 or ord(s[i])
        ans=""
        for i in s:
            ans+= str(ord(i)-96)
        print(ans)
        while k > 0:
            ans=list(ans)
            a=0
            for i in ans:
                a+=int(i)
            ans=str(a)
            k-=1
        return a