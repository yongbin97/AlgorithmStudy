import copy
import sys

sys.stdin = open("input.txt", "r")


def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end="\t")
        print()
    print()


# N: 미로의 크기
# M: 참가자 수
# K: 턴 수
N, M, K = map(int, sys.stdin.readline().split())

# 미로
maps = []
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))

# 참가자 [idx, [x, y]]
players = {}
for i in range(M):
    player_x, player_y = map(int, sys.stdin.readline().split())
    players[i] = [player_x - 1, player_y - 1]

# 출구
goal_x, goal_y = map(int, sys.stdin.readline().split())
goal = [goal_x - 1, goal_y - 1]

print_arr(maps)
print(players)


################################################################
################################################################
################################################################

# Step 1-1: goal - player 거리 구하기
def get_distance(x, y):
    global goal
    return abs(x - goal[0]) + abs(y - goal[1])


# Step 1-2: 참가자 다음 위치 구하기
def get_next_xy(x, y):
    dx_dy_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    distance = get_distance(x, y)

    for dx, dy in dx_dy_list:
        next_x, next_y = x + dx, y + dy
        dist = get_distance(next_x, next_y)
        if (
                0 <= next_x < N and 0 <= next_y < N
                and maps[next_x][next_y] == 0
                and dist < distance
        ):
            return next_x, next_y

    return -1, -1


# Step 1: 참가자 이동
def move_players():
    global players, answer

    exit_players = []
    for player_id, player_xy in players.items():
        next_x, next_y = get_next_xy(player_xy[0], player_xy[1])
        if next_x != -1:
            print(f"player{player_id} 이동 {player_xy} -> {next_x, next_y}")
            answer += 1
            if next_x == goal[0] and next_y == goal[1]:
                exit_players.append(player_id)
                print(f"player{player_id} 탈출")
            players[player_id] = [next_x, next_y]
        else:
            print(f"player{player_id} 이동 X")

    for player_id in exit_players:
        del players[player_id]


# Step 3-1: 회전
def rotate(r, c, d, x, y):
    """
    좌상단 (r, c), 회전하는 변의 길이: d
    (x, y) -> (r - c + y, r + c + d - x)
    """
    return r - c + y, r + c + d - x - 1


# Step 3-2: 회전할 최소 정사각형 구하기
def get_square():
    global goal, players

    target_r, target_c, d = N, N, N
    for player_id, (x, y) in players.items():
        curr_d = max(abs(goal[0] - x), abs(goal[1] - y))
        if curr_d <= d:
            temp_r = max(goal[0], x) - curr_d if max(goal[0], x) - curr_d >= 0 else 0
            temp_c = max(goal[1], y) - curr_d if max(goal[1], y) - curr_d >= 0 else 0
            # 정사각형의 크기가 더 작은 경우
            if curr_d < d:
                d = curr_d
                target_r, target_c = temp_r, temp_c

            # 정사각형 크기는 같으나 r, c가 더 작은 경우
            else:
                if temp_r < target_r or (temp_r == target_r and temp_c < target_c):
                    target_r, target_c = temp_r, temp_c

    return target_r, target_c, d + 1


# Step 3: 미로 회전
def rotate_maze():
    global maps, goal, players
    target_r, target_c, d = get_square()
    print(f"미로 회전: {target_r, target_c} 기준,  d: {d}")
    # 미로 회전
    temp_map = copy.deepcopy(maps)
    for row in range(target_r, target_r + d):
        for col in range(target_c, target_c + d):
            x, y = rotate(target_r, target_c, d, row, col)
            temp_map[x][y] = maps[row][col] - 1 if maps[row][col] > 0 else maps[row][col]
    maps = temp_map

    # Player 회전
    for player_id, (player_x, player_y) in players.items():
        if target_r <= player_x < target_r + d and target_c <= player_y < target_c + d:
            player_x, player_y = rotate(target_r, target_c, d, player_x, player_y)
            players[player_id] = [player_x, player_y]

    # Goal 회전
    goal_x, goal_y = rotate(target_r, target_c, d, goal[0], goal[1])
    goal = [goal_x, goal_y]


answer = 0
# MAIN
for i in range(K):
    print(f"STAGE {i + 1}")
    # print(f"GOAL: {goal}")
    print_arr(maps)
    # Step 1: 참가자 이동
    move_players()
    # Step 2: 남은 참가자 확인
    if len(players) == 0:
        break
    # Step 3: 미로 회전
    rotate_maze()

    # print(players)
    # print(answer)

print(answer)
print(goal[0] + 1, goal[1] + 1)
