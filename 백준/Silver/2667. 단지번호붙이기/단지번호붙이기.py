import sys
from collections import deque


def bfs(x, y):
    dx_list = [1, -1, 0, 0]
    dy_list = [0, 0, 1, -1]
    q = deque()
    q.append([x, y])
    ap_count = 0

    while q:
        curr_x, curr_y = q.popleft()
        visited[curr_x][curr_y] = True
        ap_count += 1

        for dx, dy in zip(dx_list, dy_list):
            next_dx = curr_x + dx
            next_dy = curr_y + dy

            if 0 <= next_dx < N and 0 <= next_dy < M:
                if maps[next_dx][next_dy] == 1 and not visited[next_dx][next_dy] and [next_dx, next_dy] not in q:
                    q.append([next_dx, next_dy])

    return ap_count


N = int(sys.stdin.readline())

maps = []
for _ in range(N):
    maps.append([int(i) for i in list(sys.stdin.readline().strip())])

M = len(maps[0])
visited = [[False] * M for _ in range(N)]

apartment_set = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1 and not visited[i][j]:
            apartment_set.append(bfs(i, j))

print(len(apartment_set))
for c in sorted(apartment_set):
    print(c)