import sys
from collections import deque

# 지도
maps = []
# 각 팀 head 집합
team_head_dict = {}
# 각 팀 정보 {tid: [팀원 위치 정보]}, head -> tail
team_dict = {}

sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/꼬리잡기놀이/input.txt", "r")
n, m, k = map(int, sys.stdin.readline().split())
tid = 0
for i in range(n):
    lines = list(map(int, sys.stdin.readline().split()))
    for j, v in enumerate(lines):
        if v == 1:
            team_head_dict[tid] = [i, j]
            tid += 1
    maps.append(lines)

# 각 좌표별 팀 정보 (i, j) = tid or -1
team_path_maps = [[-1] * n for _ in range(n)]


# TODO: 삭제
def print_map(_map):
    for i in range(n):
        print(_map[i])


print_map(maps)


# def set_team_dict():
#     dx_list = [1, -1, 0, 0]
#     dy_list = [0, 0, 1, -1]
#     visited = [[False] * n for _ in range(n)]
#     for tid, head in team_head_dict.items():
#         team_dict[tid] = [head]
#         visited[head[0]][head[1]] = True
#         team_path_maps[head[0]][head[1]] = tid
#         dq = deque()
#         dq.append(head)
#         while dq:
#             x, y = dq.popleft()
#             for dx, dy in zip(dx_list, dy_list):
#                 if 0 <= x + dx < n and 0 <= y + dy < n and not visited[x + dx][y + dy]:
#                     if maps[x + dx][y + dy] == 2:
#                         team_path_maps[x + dx][y + dy] = tid
#                         team_dict[tid].append([x + dx, y + dy])
#
#                         dq.append([x + dx, y + dy])
#                         visited[x + dx][y + dy] = True


def set_team_dict_dfs():
    dx_list = [1, -1, 0, 0]
    dy_list = [0, 0, 1, -1]
    visited = [[False] * n for _ in range(n)]

    def dfs(x, y):
        team_path_maps[x][y] = tid
        if 0 < maps[x][y] < 4:
            team_dict[tid].append([x, y])
        next_point = []
        for dx, dy in zip(dx_list, dy_list):
            if 0 <= x + dx < n and 0 <= y + dy < n and not visited[x + dx][y + dy]:
                if maps[x + dx][y + dy] > 0:
                    next_point.append([x + dx, y + dy])
                    visited[x + dx][y + dy] = True

        next_point.sort(key=lambda x: maps[x[0]][x[1]])
        for point in next_point:
            dfs(point[0], point[1])

    for tid, head in team_head_dict.items():
        visited[head[0]][head[1]] = True
        team_dict[tid] = []
        dfs(head[0], head[1])


def move():
    """
    step 1
    모든 팀 한 칸 앞으로
    """
    dx_list = [1, -1, 0, 0]
    dy_list = [0, 0, 1, -1]

    for tid, head in team_head_dict.items():
        for dx, dy in zip(dx_list, dy_list):
            if 0 <= head[0] + dx < n and 0 <= head[1] + dy < n:
                if maps[head[0] + dx][head[1] + dy] in [3, 4]:
                    team_head_dict[tid] = [head[0] + dx, head[1] + dy]

        for idx in range(len(team_dict[tid]) - 1, 0, -1):
            front_x, front_y = team_dict[tid][idx - 1]

            if idx == len(team_dict[tid]) - 1:
                maps[team_dict[tid][idx][0]][team_dict[tid][idx][1]] = 4
                maps[front_x][front_y] = 3
            else:
                maps[front_x][front_y] = 2

            team_dict[tid][idx] = [front_x, front_y]
        maps[team_head_dict[tid][0]][team_head_dict[tid][1]] = 1
        team_dict[tid][0] = team_head_dict[tid]


def set_catcher(time):
    """
    step 2 공 던지기
    round start: 0
    1. 0 <= t < n
        ball: (t, 0) -> (t, n-1)
        => row = t, min(col)

    2. n <= t < 2n
        ball: (n-1, t-n) -> (0, t-n)
        => col = t-n, max(row)

    3. 2n <= t < 3n
        ball: (3n-t-1, n-1) -> (3n-t-1, 0)
        => row = 3n-t-1, max(col)

    4. 3n <= t < 4n
        ball: (0, 4n-t-1) -> (n-1, 4n-t-1)
        => col = 4n-t-1, min(row)
    """
    time %= 4 * n
    if 0 <= time < n:
        for col in range(n):
            if maps[time][col] in [1, 2, 3]:
                return [time, col]

    elif n <= time < 2 * n:
        for row in range(n - 1, -1, -1):
            if maps[row][time - n] in [1, 2, 3]:
                return [row, time - n]

    elif 2 * n <= time < 3 * n:
        for col in range(n - 1, -1, -1):
            if maps[3 * n - time - 1][col] in [1, 2, 3]:
                return [3 * n - time - 1, col]

    else:
        for row in range(n):
            if maps[row][4 * n - time - 1] in [1, 2, 3]:
                return [row, 4 * n - time - 1]

    return None


def revert(tid):
    """
    공을 받은 tid의 팀 반대 방향으로 뒤집기
    """
    team_dict[tid] = team_dict[tid][::-1]
    head, tail = team_dict[tid][0], team_dict[tid][-1]
    team_head_dict[tid] = head
    maps[head[0]][head[1]] = 1
    maps[tail[0]][tail[1]] = 3


def add_score(catcher, score):
    """
    점수 받기
    앞에서부터 i번째 -> score += i ** 2

    """
    row, col = catcher
    tid = team_path_maps[row][col]
    idx = team_dict[tid].index([row, col])
    score += (idx + 1) ** 2

    revert(tid)

    return score


# set_team_dict()
set_team_dict_dfs()
print(team_dict)
print("path")
print_map(team_path_maps)
print()
# 점수 합
score = 0
for i in range(k):
    print(f"ROUND: {i}")
    move()
    print("after move")
    print(team_dict)
    print_map(maps)
    catcher = set_catcher(i)
    if catcher is not None:
        print(f"catcher:{catcher}")
        score = add_score(catcher, score)
    print("after get ball")
    print_map(maps)
    print(score)
