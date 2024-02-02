import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())


def bfs():
    dq = deque()
    dq.append([S, 0])
    visited = [False for _ in range(F + 1)]

    while dq:
        curr_x, curr_t = dq.popleft()

        if curr_x == G:
            return curr_t

        for dx in [U, -1 * D]:
            if 1 <= curr_x + dx <= F and not visited[curr_x + dx]:
                dq.append([curr_x + dx, curr_t + 1])
                visited[curr_x + dx] = True

    return "use the stairs"

print(bfs())