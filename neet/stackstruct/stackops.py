class MinStack:

    def __init__(self):
        self.a=[] 

    def push(self, val: int) -> None:
        self.a.append(val)
                
    def pop(self) -> None:
        x=self.a.pop() 
            
    
    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return min(self.a)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




a = []
m = []

class MinStack:        

    def push(self, val: int) -> None:
        a.append(val)
        if len(m) == 0 or val <= m[-1]:
            m.append(val)

    def pop(self) -> None:
        if len(a) > 0:
            if a[-1] == m[-1]:
                m.pop()
            a.pop()

    def top(self) -> int:
        if len(a) > 0:
            return a[-1]

    def getMin(self) -> int:
        if len(m) > 0:
            return m[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else :
            self.minstack.append(min(self.minstack[-1],val))  

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()