class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = []
        for i in tokens:
            if i not in "*/-+":
                a.append(int(i))
            else:
                x=a.pop()
                y=a.pop()
                if i == "+":
                    z=x+y
                elif i == "-":
                    z=y-x
                elif i == "*":
                    z=x*y
                elif i == "/":
                    z = int(y / x)   
                a.append(z)
        return a[0]
