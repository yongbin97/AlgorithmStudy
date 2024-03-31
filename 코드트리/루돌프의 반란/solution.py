import sys

sys.stdin = open("input.txt", "r")


def print_array(memo, arr):
    print(memo)
    # for i in range(len(arr)):
    #     for ele in arr[i]:
    #         print(ele, end="\t")
    #     print()
    # print()


class Santa:
    """
    Santa 객체
    - status = 0 or -1
        0: 정상
        -1: 기절 턴
        -2: 충돌한 턴
    """

    def __init__(self, id, r, c):
        self.id = id
        self.r = r
        self.c = c
        self.status = 0

    def update_rc(self, r, c):
        self.r = r
        self.c = c

    def __repr__(self):
        return str(self.id)


# N: 게임판 크기
# M: 게임 턴 수
# P: 산타의 수
# C: 루돌프의 힘 (루돌프 -> 산타 충돌 시, 산타 획득 점수)
# D: 산타의 힘 (산타 -> 루돌프 충돌 시, 산타 획득 점수)
N, M, P, C, D = map(int, sys.stdin.readline().split())

# 게임판
maps = [[0] * N for _ in range(N)]

# 루돌프 초기 위치
rudolph_r, rudolph_c = map(int, sys.stdin.readline().split())
rudolph_r -= 1
rudolph_c -= 1
maps[rudolph_r][rudolph_c] = -1

# 전체 산타 dict - {santa_id: Santa Object}
santa_dict = {}
# 생존한 산타 객체 리스트
alive_santa_list = []
# 각 산타 점수 리스트 (idx: 0은 허수)
santa_score_list = [0] * (P + 1)

for _ in range(P):
    santa_id, r, c = map(int, sys.stdin.readline().split())
    santa = Santa(santa_id, r - 1, c - 1)

    santa_dict[santa_id] = santa
    alive_santa_list.append(santa)
    maps[r - 1][c - 1] = santa_id

print(f"생존한 산타: {alive_santa_list}")
print_array("현황판", maps)


def collision(dr, dc, dist, santa_id):
    """
    충돌
    dr, dc: 이동 방향
    dist: 이동 거리
    santa_id: 충돌한 santa id
    """
    santa = santa_dict[santa_id]
    next_r, next_c = santa.r + dr * dist, santa.c + dc * dist
    maps[santa.r][santa.c] = 0

    print(f"[충돌] santa id: {santa_id} {santa.r, santa.c} -> {next_r, next_c}")

    # 경기장 내부
    if 0 <= next_r < N and 0 <= next_c < N:
        # 상호작용
        if maps[next_r][next_c] > 0:
            collision(dr, dc, 1, maps[next_r][next_c])

        santa.update_rc(next_r, next_c)
        maps[santa.r][santa.c] = santa.id

    # OUT
    else:
        alive_santa_list.remove(santa)
        print(f"santa{santa.id} OUT")
        print(f"현재 생존한 산타: {alive_santa_list}")


def get_direction():
    """
    현재 루돌프 기준 가장 가까운 산타 찾아서 방향 가져오기
    return [r, c]
    """
    global rudolph_r, rudolph_c
    distance = N * N

    for santa in alive_santa_list:
        if (rudolph_r - santa.r) ** 2 + (rudolph_c - santa.c) ** 2 < distance:
            target = santa
            distance = (rudolph_r - santa.r) ** 2 + (rudolph_c - santa.c) ** 2

        elif (
                (rudolph_r - santa.r) ** 2 + (rudolph_c - santa.c) ** 2 == distance
                and (
                        target.r < santa.r or target.r == santa.r and target.c < santa.c
                )
        ):
            target = santa
            distance = (rudolph_r - santa.r) ** 2 + (rudolph_c - santa.c) ** 2

    print(f"target: {target}")

    if rudolph_r > target.r:
        dr = -1
    elif rudolph_r == target.r:
        dr = 0
    else:
        dr = 1

    if rudolph_c > target.c:
        dc = -1
    elif rudolph_c == target.c:
        dc = 0
    else:
        dc = 1

    return dr, dc, target.id


def move_rudolph():
    """
    루돌프 이동
    - 가장 가까운 산타에게 돌진
        우선순위: 거리(직선 거리 작은), santa_r(큰), santa_c(큰)
    - 이동: 모든 방향 1칸씩

    충돌 시 + C점
    """
    global rudolph_r, rudolph_c

    dr, dc, target_id = get_direction()
    maps[rudolph_r][rudolph_c] = 0
    print(f"루돌프 이동: {rudolph_r, rudolph_c} -> {rudolph_r + dr, rudolph_c + dc}")
    rudolph_r += dr
    rudolph_c += dc

    # 충돌
    if maps[rudolph_r][rudolph_c] != 0:
        print(f"Rudolph 충돌 -> santa{target_id}")
        santa_dict[target_id].status = -2
        santa_score_list[target_id] += C
        collision(dr, dc, C, target_id)

    maps[rudolph_r][rudolph_c] = -1
    # print_array("루돌프 이동", maps)

    return rudolph_r, rudolph_c


def move_santa():
    """
    산타 이동
    - 1번부터 P번까지 이동
    - 루돌프에게 가까워지는 방향으로 이동
        우선순위: 거리(직선 거리 작은), 상 우 하 좌

    제약사항
    - 산타가 이미 있는 칸이나 맵 밖으로는 이동 X
    - 이동할 칸 없으면 이동 X
    - 기절, Out된 산타는 이동 X
    - 이동할 수는 있지만 현재보다 가까워지지 않는다면 이동 X
    """
    global rudolph_r, rudolph_c

    dr_dc_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for santa in sorted(alive_santa_list, key=lambda x: x.id):
        # 기절한 산타 스킵
        if santa.status < 0:
            print(f"santa{santa.id} 기절")
            continue

        min_distance = (rudolph_r - santa.r) ** 2 + (rudolph_c - santa.c) ** 2
        min_dr, min_dc = 0, 0

        for dr, dc in dr_dc_list:
            temp_r, temp_c = santa.r + dr, santa.c + dc
            distance = (rudolph_r - temp_r) ** 2 + (rudolph_c - temp_c) ** 2
            if (
                    0 <= temp_r < N and 0 <= temp_c < N
                    and maps[temp_r][temp_c] <= 0
                    and distance < min_distance
            ):
                min_distance = distance
                min_dr, min_dc = dr, dc

        print(f"Santa{santa.id} 이동: {santa.r, santa.c} -> {santa.r + min_dr, santa.c + min_dc}")
        next_r, next_c = santa.r + min_dr, santa.c + min_dc

        # 충돌
        if maps[next_r][next_c] == -1:
            print(f"santa{santa.id} -> Rudolph 충돌")
            santa.status = -2
            santa_score_list[santa.id] += D
            collision(-1 * min_dr, -1 * min_dc, D - 1, santa.id)
            # print_array(f"santa{santa.id} 이동", maps)

        else:
            maps[santa.r][santa.c] = 0
            santa.update_rc(next_r, next_c)
            maps[next_r][next_c] = santa.id
            # print_array(f"santa{santa.id} 이동", maps)


# Main
for i in range(M):
    print(f"=======STAGE {i + 1}=======")
    # 루돌프 이동 -> 충돌 -> 상호작용
    move_rudolph()
    # 산타 이동 -> 충돌 -> 상호작용
    move_santa()
    # 생존한 산타 여부 확인
    # 생존한 산타 + 1 점
    if alive_santa_list:
        print(f"생존한 산타: {sorted(alive_santa_list, key=lambda x: x.id)}")
        for santa in alive_santa_list:
            santa_score_list[santa.id] += 1
            if santa.status < 0:
                santa.status += 1
    else:
        print("모든 산타가 탈락하였습니다.")
        break
    print(f"현재 점수: {santa_score_list[1:]}")
    print()

for score in santa_score_list[1:]:
    print(score, end=" ")
