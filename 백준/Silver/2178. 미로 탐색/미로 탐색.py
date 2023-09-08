import sys
from collections import deque


# get data
n, m = map(int, sys.stdin.readline().split())
maps = []
for _ in range(n):
    maps.append([int(i) for i in sys.stdin.readline().strip()])

result = [[0] * m for _ in range(n)]

def bfs():
    q = deque()
    q.append((0,0))
    result[0][0] = 1
    dx_list = [1, -1, 0, 0]
    dy_list = [0, 0, 1, -1]

    while len(q) > 0:
        x, y = q.popleft()

        # next loc
        for dx, dy in zip(dx_list, dy_list):
            next_x = x + dx
            next_y = y + dy

            # outside
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue
            # wall
            if maps[next_x][next_y] == 1 and result[next_x][next_y] == 0:
                result[next_x][next_y] = result[x][y] + 1
                q.append((next_x, next_y))

    return result[n-1][m-1]

print(bfs())
