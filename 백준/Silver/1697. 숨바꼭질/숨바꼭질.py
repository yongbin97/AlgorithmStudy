import sys
from collections import deque


def bfs(start, target):
    dq = deque()
    dq.append(start)

    dist = [0] * 100001

    while dq:
        idx = dq.popleft()
        if idx == target:
            return dist[idx]
        
        for next_idx in [idx - 1, idx + 1, idx * 2]:
            if 0 <= next_idx < 100001 and not dist[next_idx]:
                dist[next_idx] = dist[idx] + 1
                dq.append(next_idx)


N, K = map(int, sys.stdin.readline().split())

print(bfs(N, K))
