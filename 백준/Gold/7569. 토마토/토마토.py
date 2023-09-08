import sys
from collections import deque

M, N, H = list(map(int, sys.stdin.readline().split()))

boxes = []
q = deque()

for h in range(H):
    box = []
    for i in range(N):
        box.append(list(map(int, sys.stdin.readline().split())))
        for j in range(M):
            if box[i][j] == 1:
                q.append([i, j, h])
    boxes.append(box)

def bfs():
    dx_list = [1, -1, 0, 0, 0, 0]
    dy_list = [0, 0, 1, -1, 0, 0]
    dz_list = [0, 0, 0, 0, 1, -1]

    while q:
        curr_x, curr_y, curr_z = q.popleft()
        curr_tomato = boxes[curr_z][curr_x][curr_y]

        for dx, dy, dz in zip(dx_list, dy_list, dz_list):
            dx_next, dy_next, dz_next = curr_x + dx, curr_y + dy, curr_z + dz

            if 0 <= dx_next < N and 0 <= dy_next < M and 0 <= dz_next < H:
                if boxes[dz_next][dx_next][dy_next] == 0:
                    boxes[dz_next][dx_next][dy_next] = curr_tomato + 1
                    q.append([dx_next, dy_next, dz_next])

def get_max_day():
    max_day = 0
    for layer in boxes:
        for tomato in layer:
            for t in tomato:
                if t == 0:
                    return -1
                max_day = max(t, max_day)

    return max_day - 1


bfs()
print(get_max_day())
