class Router:

    def __init__(self, memoryLimit: int):
        self.arr=[]
        self.l=memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if len(self.arr) < self.l:
            if [source, destination, timestamp] in self.arr:
                return False
            else:
                self.arr.append([source, destination, timestamp])
        else:
            if [source, destination, timestamp] in self.arr:
                return False
            self.arr=self.arr[1:]
            self.arr.append([source, destination, timestamp])
        
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.arr) > 0:
            x=self.arr[0]
            self.arr=self.arr[1:]
            return x
        else:
            return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        c=0
        # for i in self.arr:
        #     if i[1]==destination and i[2]>= startTime and i[2] <= endTime:
        #         c+=1
        l=0
        r=len(self.arr) - 1
        # while l<=r:
        #     if self.arr[l][2] == startTime:
        #         break
        #     elif  startTime < self.arr[(r+l)//2][2]   :
        #         r= (r+l)//2
        #     else:
        #         l= (r+l)//2
        while l <= r:
            mid = (l + r) // 2
            if self.arr[mid][2] < startTime:
                l = mid + 1
            else:
                r = mid - 1

        # for i in range(l,self.l):
        #     if self.arr[i][1]== destination and self.arr[i][2] >= startTime and self.arr[i][2] >= endTime:
        #         c+=0
        #     if self.arr[i][2] > endTime:
        #         break
        i = l
        while i < len(self.arr) and self.arr[i][2] <= endTime:
            if self.arr[i][1] == destination:
                c += 1
            i += 1
        return c


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)