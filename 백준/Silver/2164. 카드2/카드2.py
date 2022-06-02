import sys
from collections import deque

N = int(sys.stdin.readline())

stk = deque(range(1, N+1))

for _ in range(N):
    if len(stk) == 1:
        print(stk.pop())
    else:
        stk.popleft()
        tmp = stk.popleft()
        stk.append(tmp)
