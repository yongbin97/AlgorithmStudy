import sys
from collections import deque

sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/정육면체 굴리기/input.txt", "r")

direction = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}


def print_map(_map):
    for row in _map:
        print(row)


class Dice:
    def __init__(self):
        self.r = 0
        self.c = 0
        self.d = 0
        self.x1 = 2
        self.x2 = 5
        self.y1 = 3
        self.y2 = 4
        self.z1 = 1
        self.z2 = 6

    def _move_left(self):
        self.y1, self.y2, self.z1, self.z2 = self.z2, self.z1, self.y1, self.y2

    def _move_right(self):
        self.y1, self.y2, self.z1, self.z2 = self.z1, self.z2, self.y2, self.y1

    def _move_down(self):
        self.x1, self.x2, self.z1, self.z2 = self.z1, self.z2, self.x2, self.x1

    def _move_up(self):
        self.x1, self.x2, self.z1, self.z2 = self.z2, self.z1, self.x1, self.x2

    def move(self):
        print(self.d)
        if self.d == 0:
            self._move_right()
        elif self.d == 1:
            self._move_down()
        elif self.d == 2:
            self._move_left()
        else:
            self._move_up()

        self.r += direction[self.d][0]
        self.c += direction[self.d][1]

        return self.r, self.c

    def rotate(self, num):
        print(f"z2: {self.z2}, num:{num}")
        if self.z2 > num:
            self.d = (self.d + 1) % 4
            print("90도 회전")
        elif self.z2 < num:
            self.d = (self.d - 1) % 4
            print("-90도 회전")

        if not (0 <= self.r + direction[self.d][0] < n and 0 <= self.c + direction[self.d][1] < n):
            print("반대방향")
            self.d = (self.d + 2) % 4


# n: 격자 크기, m: 반복 횟수
n, m = map(int, sys.stdin.readline().split())
# 격자 판
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

# 점수판
score_map = [[0] * n for _ in range(n)]


def set_score_map():
    """
    점수판
    score_map[i][j] => i, j에서 얻을 수 있는 점수
    """
    visited = [[False] * n for _ in range(n)]
    dr_list = [1, -1, 0, 0]
    dc_list = [0, 0, 1, -1]

    def bfs(r, c):
        num = maps[r][c]
        dq = deque([(r, c)])
        same_num_list = [(r, c)]
        visited[r][c] = True

        while dq:
            curr_r, curr_c = dq.popleft()

            for dr, dc in zip(dr_list, dc_list):
                next_r, next_c = curr_r + dr, curr_c + dc
                if 0 <= next_r < n and 0 <= next_c < n and not visited[next_r][next_c] and maps[next_r][next_c] == num:
                    dq.append((next_r, next_c))
                    visited[next_r][next_c] = True
                    same_num_list.append((next_r, next_c))

        for x, y in same_num_list:
            score_map[x][y] = len(same_num_list) * num

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)


score = 0
dice = Dice()
set_score_map()
for _ in range(m):
    curr_r, curr_c = dice.move()
    print(f"{curr_r, curr_c}, 점수: {score_map[curr_r][curr_c]}")
    score += score_map[curr_r][curr_c]
    dice.rotate(maps[curr_r][curr_c])
print(score)
