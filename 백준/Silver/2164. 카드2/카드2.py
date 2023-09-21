import sys
from collections import deque


N = int(sys.stdin.readline())

dq = deque([i for i in range(1, N+1)])
while len(dq) != 1:
    _ = dq.popleft()
    second = dq.popleft()
    dq.append(second)

print(dq.pop())