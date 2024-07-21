class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s=[]
        for i in logs:
            if i=="../":
                if len(s) > 0:
                    s.pop()
            elif i == "./":
                continue
            else:
                s.append(i)
        return len(s)


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        a=0
        o=["./","../"]
        for i in logs:
            if i not in o:
                a+=1
            else:
                if i == o[1] and a > 0:
                    a-=1
        return a


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        a=0
        b=0
        for i in logs:
            if i != "./" and i != "../":
                a+=1
            else:
                if i == "../":
                    b+=1
        return a-b if a > b else 0