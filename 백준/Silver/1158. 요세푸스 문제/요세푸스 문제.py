import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
deq_list = deque(range(1, n+1))
answ_list = list()

for _ in range(n):
    for _ in range(k-1):
        temp = deq_list.popleft()
        deq_list.append(temp)
    answ_list.append(str(deq_list.popleft()))

answ_str = ', '.join(answ_list)
answ_str = "<" + answ_str + ">"
print(answ_str)