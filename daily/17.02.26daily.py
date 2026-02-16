class Solution:
    def reverseBits(self, n: int) -> int:
        # print(int(bin(n),2)==n)
        s=""
        s=str(bin(n))
        print(s)
        a=s[:2]
        s=s[2:]
        print(len(s))
        z=32-len(s)
        zz='0'*z
        print(zz)
        s=zz+s
        s=a+s[::-1]
        print(s)
        x=int(s,2)
        return x