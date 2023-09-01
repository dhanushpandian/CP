class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((timestamp,value))
        else:
            self.dic[key] = [(timestamp , value)]
     
    def get(self, key: str, timestamp: int) -> str:
        if key in self.dic:
            for i in range(len(self.dic[key])-1,-1,-1):
                t,v = self.dic[key][i]
                if t<=timestamp:
                    return v
            return ""
        return ""
        

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)