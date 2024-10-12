import sys
from collections import deque


# Solution
def search(N, maps):
    visited = [[sys.maxsize] * N for _ in range(N)]
    dq = deque()
    dq.append([0, 0, maps[0][0]])  # i, j, cnt
    visited[0][0] = maps[0][0]

    while dq:
        x, y, cnt = dq.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, N) and visited[nx][ny] > cnt + maps[nx][ny]:
                dq.append([nx, ny, cnt + maps[nx][ny]])
                visited[nx][ny] = cnt + maps[nx][ny]

    return visited[N - 1][N - 1]


def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N


# Main
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
idx = 1
while True:
    N = int(sys.stdin.readline().strip())

    if N == 0:
        break

    maps = []
    for _ in range(N):
        maps.append(list(map(int, sys.stdin.readline().split())))

    print(f"Problem {idx}: {search(N, maps)}")
    idx += 1
