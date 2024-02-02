import sys
from collections import deque

N = int(sys.stdin.readline().strip())
maps = []

for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))

dr_list = [1, -1, 0, 0]
dc_list = [0, 0, 1, -1]


def bfs(start_r, start_c, curr_h, visited):
    dq = deque()
    dq.append([start_r, start_c])
    visited[start_r][start_c] = True

    while dq:
        curr_r, curr_c = dq.popleft()

        for dr, dc in zip(dr_list, dc_list):
            next_r, next_c = curr_r + dr, curr_c + dc
            if (
                    0 <= next_r < N
                    and 0 <= next_c < N
                    and maps[next_r][next_c] > curr_h
                    and not visited[next_r][next_c]
            ):
                visited[next_r][next_c] = True
                dq.append([next_r, next_c])
    return visited


def solution():
    h = 0
    answer = 0

    while h <= 100:
        visited = []
        for _ in range(N):
            visited.append([False for _ in range(N)])

        count = 0
        for r in range(N):
            for c in range(N):
                if maps[r][c] > h and not visited[r][c]:
                    visited = bfs(r, c, h, visited)
                    count += 1
        if count == 0:
            return answer

        answer = max(answer, count)
        h += 1


print(solution())
