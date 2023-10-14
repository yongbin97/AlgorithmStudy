import sys
from collections import deque

sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/포탑부수기/input.txt", "r")


def print_map(_map):
    for line in _map:
        print(line)


class Turret:
    def __init__(self, t_id, attk, row, col):
        self.id = t_id
        self.attk = attk
        self.last_attk = 0
        self.row = row
        self.col = col

    def __lt__(self, other):
        if self.attk != other.attk:
            return self.attk < other.attk
        if self.last_attk != other.last_attk:
            return self.last_attk > other.last_attk
        if self.row + self.col != other.row + other.col:
            return self.row + self.col > other.row + other.col
        return self.col > other.col

    def __repr__(self):
        return f"{self.id}"


N, M, K = map(int, sys.stdin.readline().split())
# 포탑 지도 (id값 기록, 0 = 파괴된 포탑)
turret_map = []
# 살아있는 포탑 리스트
alive_turret_list = []

idx = 1
for i in range(N):
    turret_list = []
    turret_row = list(map(int, sys.stdin.readline().split()))
    for j, v in enumerate(turret_row):
        if v > 0:
            new_turret = Turret(idx, v, i, j)
            alive_turret_list.append(new_turret)
            turret_list.append(idx)
            idx += 1
        else:
            turret_list.append(0)
    turret_map.append(turret_list)


def razor_attk(attacker, target):
    """
    레이저 공경
    attacker -> target
    """
    dr_list = [0, 1, 0, -1]
    dc_list = [1, 0, -1, 0]
    visited = [[False] * M for _ in range(N)]

    dq = deque()
    dq.append([(attacker.row, attacker.col), []])

    while dq:
        (row, col), path = dq.popleft()

        for dr, dc in zip(dr_list, dc_list):
            next_r = (row + dr) % N
            next_c = (col + dc) % M

            if (next_r, next_c) == (target.row, target.col):
                return path + [turret_map[next_r][next_c]]

            if turret_map[next_r][next_c] > 0 and not visited[next_r][next_c]:
                dq.append([(next_r, next_c), path + [turret_map[next_r][next_c]]])
                visited[next_r][next_c] = True

    return None


def bomb_attack(attacker, target):
    path = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            row = (target.row + i) % N
            col = (target.col + j) % M
            if turret_map[row][col] > 0 and turret_map[row][col] != attacker.id:
                path.append(turret_map[row][col])

    return path


def update_turret(path, attacker, target):
    dead_turret_list = []
    for turret in alive_turret_list:
        if turret.id in path:
            if turret.id == target.id:
                turret.attk -= attacker.attk
            else:
                turret.attk -= attacker.attk // 2

            if turret.attk <= 0:
                dead_turret_list.append(turret)
        else:
            if turret.id != attacker.id:
                turret.attk += 1

    for turret in dead_turret_list:
        alive_turret_list.remove(turret)
        turret_map[turret.row][turret.col] = 0


# 최초 정렬
alive_turret_list.sort()
for i in range(1, K + 1):
    attacker = alive_turret_list[0]
    target = alive_turret_list[-1]
    attacker.attk += N + M
    attacker.last_attk = i
    print(attacker, target)

    path = razor_attk(attacker, target)
    if path is None:
        path = bomb_attack(attacker, target)

    update_turret(path, attacker, target)
    if len(alive_turret_list) == 1:
        break
    alive_turret_list.sort()

    print_map(turret_map)
print(alive_turret_list[-1].attk)
