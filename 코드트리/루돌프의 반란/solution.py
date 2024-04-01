import sys

sys.stdin = open("input.txt", "r")


def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == rudolph[0] and j == rudolph[1]:
                print("R", end="\t")
            elif arr[i][j] == 0:
                print("_", end="\t")
            else:
                print(arr[i][j], end="\t")
        print()
    print()


# N: 게임판의 크기
# M: 게임 턴 수
# P: 산타의 수
# C: 루돌프의 힘
# D: 산타의 힘
N, M, P, C, D = map(int, sys.stdin.readline().split())

# 루돌프 초기 위치
ru_r, ru_c = map(int, sys.stdin.readline().split())
rudolph = [ru_r - 1, ru_c - 1]

# 산타 위치 표기 지도
maps = [[0] * N for _ in range(N)]

# 산타 dict => id: [[r, c], status]
santa_dict = {}
# 생존한 산타 목록
alive_santa_list = []
# 산타 상태 - status = 0 정상, < 0 기절, >0 탈락
santa_status_list = [0] * (P + 1)
# 산타 점수 리스트 idx = 0은 허수
santa_score_list = [0] * (P + 1)
for _ in range(P):
    s_id, s_r, s_c = map(int, sys.stdin.readline().split())
    alive_santa_list.append(s_id)
    santa_dict[s_id] = [s_r - 1, s_c - 1]
    maps[s_r - 1][s_c - 1] = s_id


#####################################################################
#####################################################################
#####################################################################
# Step 0-1: 거리 구하기
def get_distance(r, c):
    global rudolph
    return (rudolph[0] - r) ** 2 + (rudolph[1] - c) ** 2


# Step 0-2: 충돌
def collision(direction, r, c, dist):
    """
    direction = [dr, dc]: 충돌 방향
    r,c : 충돌이 일어난 위치
    dist: 밀려나는 거리
    """
    global santa_dict, santa_score_list

    target_santa_id = maps[r][c]
    next_r, next_c = r + direction[0] * dist, c + direction[1] * dist
    # santa 정보 업데이트
    santa_dict[target_santa_id] = [next_r, next_c]
    santa_status_list[target_santa_id] = -2

    # 맵 내부
    if 0 <= next_r < N and 0 <= next_c < N:
        if maps[next_r][next_c] != 0:
            interaction(direction, next_r, next_c)
        maps[next_r][next_c] = target_santa_id

    # 맵 외부: OUT
    else:
        alive_santa_list.remove(target_santa_id)
        santa_status_list[target_santa_id] = 1
        print(f"santa{target_santa_id} out")
        print(f"현재 생존한 산타: {sorted(alive_santa_list)}")

    maps[r][c] = 0

    # 점수 획득
    santa_score_list[target_santa_id] += dist


# Step 0-3: 상호작용
def interaction(direction, r, c):
    global santa_dict

    next_r, next_c = r + direction[0], c + direction[1]
    print(f"santa{maps[r][c]} 상호작용 {r, c} -> {next_r, next_c}")

    # 맵 내부
    if 0 <= next_r < N and 0 <= next_c < N:
        if maps[next_r][next_c] != 0:
            interaction(direction, next_r, next_c)
        maps[next_r][next_c] = maps[r][c]
        santa_dict[maps[r][c]] = [next_r, next_c]

    # 맵 외부: OUT
    else:
        out_santa_id = maps[r][c]
        alive_santa_list.remove(out_santa_id)
        santa_status_list[out_santa_id] = 1
        print(f"santa{out_santa_id} 탈락")
        print(f"현재 생존한 산타: {sorted(alive_santa_list)}")

    maps[r][c] = 0


# Step 1-2: target santa 찾기
def get_target_santa():
    min_dist = 2 * (N ** 2)
    target_id = -1
    for santa_id in alive_santa_list:
        santa_r, santa_c = santa_dict[santa_id]
        dist = get_distance(santa_r, santa_c)

        # 타겟이 정해지지 않았거나, 더 가까운 산타인 경우
        if target_id == -1 or dist < min_dist:
            target_id = santa_id
            min_dist = dist

        # 현재 타겟과 거리 같은 경우
        elif target_id != -1 and dist == min_dist:
            # r이 크거나, r은 같고 c가 큰 경우
            if (
                    santa_r > santa_dict[target_id][0]
                    or (santa_r == santa_dict[target_id][0]
                        and santa_c > santa_dict[target_id][1]
            )
            ):
                target_id = santa_id
                min_dist = dist
    return target_id


# Step 1-1: 이동할 방향 찾기
def get_rudolph_direction():
    global santa_dict, rudolph

    target_id = get_target_santa()
    print(f"target: {target_id}")
    target_r, target_c = santa_dict[target_id]
    direction = [0, 0]

    # 방향 구하기
    if rudolph[0] > target_r:
        direction[0] = -1
    elif rudolph[0] < target_r:
        direction[0] = 1

    if rudolph[1] > target_c:
        direction[1] = -1
    elif rudolph[1] < target_c:
        direction[1] = 1

    return direction


# Step 1: 루돌프 이동
def move_rudolph():
    global rudolph
    direction = get_rudolph_direction()

    # 루돌프 이동
    x, y = rudolph
    rudolph[0] += direction[0]
    rudolph[1] += direction[1]
    print(f"루돌프 이동 {x, y} -> {rudolph}")

    # 충돌 확인
    if maps[rudolph[0]][rudolph[1]] != 0:
        # 충돌 발생
        print(f"루돌프 -> santa{maps[rudolph[0]][rudolph[1]]} 충돌")
        collision(direction, rudolph[0], rudolph[1], C)


# Step 2-1: 산타 이동방향 찾기
def get_santa_direction(santa_r, santa_c):
    dr_dc_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    distance = get_distance(santa_r, santa_c)
    direction = [0, 0]

    for dr, dc in dr_dc_list:
        next_r, next_c = santa_r + dr, santa_c + dc
        if 0 <= next_r < N and 0 <= next_c < N and maps[next_r][next_c] == 0:
            dist = get_distance(next_r, next_c)
            if dist < distance:
                direction = [dr, dc]
                distance = dist

    return direction


# Step 2: 산타 이동
def move_santa():
    global santa_dict, rudolph

    for santa_id in sorted(alive_santa_list):
        if santa_status_list[santa_id] == 0:
            santa_r, santa_c = santa_dict[santa_id]
            direction = get_santa_direction(santa_r, santa_c)

            if direction[0] != 0 or direction[1] != 0:
                next_r, next_c = santa_r + direction[0], santa_c + direction[1]
                print(f"santa{santa_id} 이동: {santa_r, santa_c} -> {next_r, next_c}")
                maps[next_r][next_c] = santa_id
                maps[santa_r][santa_c] = 0
                santa_dict[santa_id] = [next_r, next_c]

                # 충돌 확인
                if next_r == rudolph[0] and next_c == rudolph[1]:
                    print(f"santa{santa_id} -> 루돌프 충돌")
                    direction = [direction[0] * -1, direction[1] * -1]
                    collision(direction, next_r, next_c, D)


# Step 3: 생존한 산타 점수 추가
def add_score_to_alive_santa():
    global santa_score_list

    for santa_id in alive_santa_list:
        santa_score_list[santa_id] += 1
        if santa_status_list[santa_id] < 0:
            santa_status_list[santa_id] += 1


# MAIN
for i in range(M):
    print(f"STAGE {i + 1}")
    print_arr(maps)
    # Step 1: 루돌프 이동
    move_rudolph()
    # Step 2: 산타 이동
    move_santa()
    if len(alive_santa_list) == 0:
        break
    # Step 3: 생존한 산타 점수 추가
    add_score_to_alive_santa()
    print(f"생존자: {alive_santa_list}")
    print(f"score: {santa_score_list}")
    print()

print(" ".join(map(str, santa_score_list[1:])))
