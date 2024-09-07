class LRUCache:
    def __init__(self, capacity: int):
        self.d = {}
        self.size = 0
        self.maxsize = capacity
        self.arr = []

    def get(self, key: int) -> int:
        if key in self.d:
            self.arr.remove(key)
            self.arr.append(key)
            return self.d[key]
        else:
            return -1            

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.arr.remove(key)
            self.size -= 1
        elif self.size >= self.maxsize:
            lru_key = self.arr.pop(0)
            del self.d[lru_key]
            self.size -= 1
        
        self.d[key] = value
        self.arr.append(key)
        self.size += 1

