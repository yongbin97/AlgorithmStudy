import sys
from collections import deque


# solution
def search():
    visited = [[sys.maxsize] * N for _ in range(M)]

    dq = deque()
    dq.append([0, 0, 0])  # x, y, cnt
    visited[0][0] = 0

    while dq:
        x, y, cnt = dq.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if not in_range(nx, ny):
                continue

            next_cnt = cnt
            if maps[nx][ny] == 1:
                next_cnt = cnt + 1

            if visited[nx][ny] > next_cnt:
                dq.append([nx, ny, next_cnt])
                visited[nx][ny] = next_cnt

    return visited[M - 1][N - 1]


def in_range(x, y):
    return 0 <= x < M and 0 <= y < N


# main
N, M = map(int, sys.stdin.readline().split())
maps = []
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# get map
for _ in range(M):
    maps.append(list(map(int, sys.stdin.readline().strip())))

print(search())
