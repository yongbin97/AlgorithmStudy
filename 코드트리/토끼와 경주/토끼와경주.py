import sys


class Rabbit:
    def __init__(self, pid: int, d: int):
        self.pid = pid
        self.d = d
        self.score = 0
        self.jump_count = 0
        self.row = 0
        self.col = 0

    def __str__(self):
        return f"[pid:{self.pid}, curr:({self.row}, {self.col}), d:{self.d}, score:{self.score}, jump:{self.jump_count}]"

    def __repr__(self):
        return f"[pid:{self.pid}, curr:({self.row}, {self.col}), d:{self.d}, score:{self.score}, jump:{self.jump_count}]"


Q = int(sys.stdin.readline())
first_op = list(map(int, sys.stdin.readline().split()))
N, M, P = first_op[1:4]

rabbit_dict = {}
for i in range(P):
    pid = first_op[2 * i + 4]
    d = first_op[2 * i + 5]
    rabbit_dict[pid] = Rabbit(pid, d)


def set_racer_rabbit() -> Rabbit:
    rabbit = sorted(rabbit_dict.values(), key=lambda r: (r.jump_count, r.row + r.col, r.row, r.col, r.pid))[0]
    rabbit.jump_count += 1
    return rabbit


def move(rabbit: Rabbit):
    dr_list = [rabbit.d, -1 * rabbit.d, 0, 0]
    dc_list = [0, 0, rabbit.d, -1 * rabbit.d]

    next_list = []
    for dr, dc in zip(dr_list, dc_list):
        next_r = (rabbit.row + dr) % (2 * N - 2)
        next_c = (rabbit.col + dc) % (2 * M - 2)

        if next_r >= N:
            next_r = 2 * N - 2 - next_r

        if next_c >= M:
            next_c = 2 * N - 2 - next_c

        next_list.append([next_r, next_c])

    row, col = sorted(next_list, key=lambda x: (-(x[0] + x[1]), -x[0], -x[1]))[0]
    rabbit.row, rabbit.col = row, col
    for pid, r in rabbit_dict.items():
        if pid != rabbit.pid:
            r.score += row + col + 2


def add_score(jump_rabbit_pid_list, s):
    jump_rabbits = [rabbit_dict[pid] for pid in jump_rabbit_pid_list]
    rabbit = sorted(jump_rabbits, key=lambda r: (-(r.row + r.col), -r.row, -r.col, -r.pid))[0]
    rabbit.score += s


for _ in range(Q - 1):
    op_list = list(map(int, sys.stdin.readline().split()))

    # 경주 진행
    if op_list[0] == 200:
        jump_rabbit_pid_list = []
        for _ in range(op_list[1]):
            rabbit = set_racer_rabbit()
            jump_rabbit_pid_list.append(rabbit.pid)
            move(rabbit)
        add_score(jump_rabbit_pid_list, op_list[2])

    # 이동거리 변경
    elif op_list[0] == 300:
        rabbit_dict[op_list[1]].d *= op_list[2]

    # 경기 끝
    else:
        winner = sorted(rabbit_dict.values(), key=lambda r: -r.score)[0]
        print(winner.score)
