import sys

sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/청소는 즐거워/input.txt", "r")


def print_map(_map):
    for line in _map:
        print(line)


N = int(sys.stdin.readline())

# 먼지 현황 맵
dust_map = []
for _ in range(N):
    dust_map.append(list(map(int, sys.stdin.readline().split())))

# 방향 전환 위치 체크 맵
direction_map = [[False] * N for _ in range(N)]
for a in range(N // 2):
    direction_map[N // 2 - a][N // 2 - a - 1] = True
    direction_map[N // 2 + a + 1][N // 2 - a - 1] = True
    direction_map[N // 2 + a + 1][N // 2 + a + 1] = True
    direction_map[N // 2 - a - 1][N // 2 + a + 1] = True

# 방향  좌 하 우 상
direction = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}


def move_curr(curr_loc, d_id):
    """
    빗자루 현재 위치 이동
    """
    return [curr_loc[0] + direction[d_id][0], curr_loc[1] + direction[d_id][1]]


def up_down_direction(curr_loc, d_id):
    x, y = curr_loc
    dx = direction[d_id][0]
    direction_dict = {
        0.1: [(x + dx, y + 1), (x + dx, y - 1)],
        0.07: [(x, y + 1), (x, y - 1)],
        0.05: [(x + 2 * dx, y)],
        0.02: [(x, y + 2), (x, y - 2)],
        0.01: [(x - dx, y + 1), (x - dx, y - 1)]
    }
    return direction_dict


def left_right_direction(curr_loc, d_id):
    x, y = curr_loc
    dy = direction[d_id][1]
    direction_dict = {
        0.1: [(x - 1, y + dy), (x + 1, y + dy)],
        0.07: [(x + 1, y), (x - 1, y)],
        0.05: [(x, y + 2 * dy)],
        0.02: [(x + 2, y), (x - 2, y)],
        0.01: [(x + 1, y - dy), (x - 1, y - dy)]
    }
    return direction_dict


def move_dust(curr_loc, d_id, answer):
    """
    먼지 이동
    d % 2 == 0: 좌우 이동
    d % 2 == 1: 상하 이동
    """
    if d % 2 == 0:
        direction_dict = left_right_direction(curr_loc, d_id)
    else:
        direction_dict = up_down_direction(curr_loc, d_id)
    x, y = curr_loc
    curr_dust = dust_map[x][y]

    sum_dust = 0
    for rate, xy_list in direction_dict.items():
        for r, c in xy_list:
            sum_dust += int(curr_dust * rate)
            if 0 <= r < N and 0 <= c < N:
                dust_map[r][c] += int(curr_dust * rate)
            else:
                answer += int(curr_dust * rate)

    dx, dy = direction[d_id]
    if 0 <= x + dx < N and 0 <= y + dy < N:
        dust_map[x + dx][y + dy] += curr_dust - sum_dust
    else:
        answer += curr_dust - sum_dust
    dust_map[x][y] = 0
    return answer


def rotate_direction(curr_loc, d_i):
    if direction_map[curr_loc[0]][curr_loc[1]]:
        return (d_i + 1) % 4
    else:
        return d_i


# 빗자루 현재 위치
curr = [N // 2, N // 2]
# 빗자루 방향
d = 0
# 정답: 격자 박으로 떨어지는 먼지 양
answer = 0
while curr != [0, 0]:
    # 1. 빗자루 이동
    curr = move_curr(curr, d)
    # 2. 먼지 이동
    answer = move_dust(curr, d, answer)
    # 3. 빗자루 방향 업데이트
    d = rotate_direction(curr, d)

    print_map(dust_map)
    print()

print(answer)
