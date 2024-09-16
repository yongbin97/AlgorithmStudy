import sys
from collections import deque


R, C = map(int, sys.stdin.readline().split())
maps = []

for _ in range(R):
    maps.append(list(sys.stdin.readline().strip()))

N = int(sys.stdin.readline())
h_list = []

for h in list(map(int, sys.stdin.readline().split())):
    h_list.append(R - h)


def print_graph(graph):
    for i, row in enumerate(graph):
        for col in row:
            print(col, end="")
        if i < R - 1:
            print()


def in_range(r, c):
    return 0 <= r < R and 0 <= c < C


def throw(height, idx):
    if idx % 2 == 0:
        c = 0
        dc = 1
    else:
        c = C - 1
        dc = -1

    while in_range(height, c) and maps[height][c] != "x":
        c += dc

    if in_range(height, c):
        maps[height][c] = "."


def bfs(r, c, visited):
    if r == R - 1:
        return False, None

    cluster = [[False] * C for _ in range(R)]
    dq = deque()
    dq.append([r, c])
    visited[r][c] = True
    cluster[r][c] = True

    while dq:
        cr, cc = dq.popleft()
        visited[cr][cc] = True
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr = cr + dr
            nc = cc + dc

            if in_range(nr, nc) and maps[nr][nc] == "x" and not cluster[nr][nc]:
                cluster[nr][nc] = True

                if nr == R - 1:
                    return False, None

                dq.append([nr, nc])

    return True, cluster


def find_floating_cluster():
    visited = [[False] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if maps[i][j] == "x" and not visited[i][j]:
                is_cluster, cluster = bfs(i, j, visited)
                if is_cluster:
                    return cluster
    return None


def search(col, cluster):
    start = None

    for i in range(R):
        if cluster[i][col]:
            start = i

    if start is not None:
        for i in range(start + 1, R):
            if maps[i][col] == "x":
                return i - start - 1

        return R - start - 1

    return start


def find_length_of_move(cluster):
    length = R

    for j in range(C):
        tmp = search(j, cluster)
        if tmp is not None:
            length = min(length, tmp)

    return length if length < R else 0


def move(d, cluster):
    for j in range(C):
        for i in range(R - 1, -1, -1):
            if cluster[i][j]:
                maps[i + d][j] = "x"
                maps[i][j] = "."


def gravity():
    cluster = find_floating_cluster()
    if cluster is None:
        return

    length = find_length_of_move(cluster)
    if length > 0:
        move(length, cluster)


for idx in range(N):
    throw(h_list[idx], idx)
    gravity()

print_graph(maps)
