from collections import deque
d=deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)
d.extend([1,2,3,4,5,6,7])
print(d)
d.extendleft([8,9,10])
print(d)
d.rotate(2)
print(d)
d.rotate(-1)
print(d)



