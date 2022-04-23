

from collections import deque

dq = deque(range(10), maxlen=10)

print(dq)

dq.rotate(3)

print(dq)

dq.rotate(-4)

print(dq)

dq.appendleft(-1)

print(dq)

dq.extend([10, 20, 30, 40])
print(dq)

dq.extendleft([11, 22, 33, 44])
print(dq)
