import sys
import heapq
from collections import defaultdict, Counter

sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/놀이기구 탑승/input.txt", "r")


def print_map(_map):
    for r in _map:
        print(r)


N = int(sys.stdin.readline())

surround_dr_dc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 빈칸 수 PQ
# (row, col)
empty_count_dict = defaultdict(list)

# 빈칸 수 map
empty_count_map = []
for i in range(N):
    tmp_row = []
    for j in range(N):
        if i == 0 or j == 0 or i == N - 1 or j == N - 1:
            if i in [0, N - 1] and j in [0, N - 1]:
                heapq.heappush(empty_count_dict[2], (i, j))
                tmp_row.append(-2)
            else:
                heapq.heappush(empty_count_dict[3], (i, j))
                tmp_row.append(-3)
        else:
            heapq.heappush(empty_count_dict[4], (i, j))
            tmp_row.append(-4)
    empty_count_map.append(tmp_row)

# 주변 좋아하는 친구 수
fav_friends_count = [[0] * N for _ in range(N)]


def get_max_empty_count():
    """
    인접한 칸 중 비어있는 칸이 많은 칸
    """
    _count = max(empty_count_dict.keys())
    while not empty_count_dict[_count]:
        del empty_count_dict[_count]
        _count = max(empty_count_dict.keys())
    return heapq.heappop(empty_count_dict[_count])


def find_most_common(friend_r_c_list):
    """
    좋아하는 친구가 많은 칸 찾기
    """
    tmp_r_c_list = []
    for row, col in friend_r_c_list:
        for dr, dc in surround_dr_dc:
            if 0 <= row + dr < N and 0 <= col + dc < N and empty_count_map[row + dr][col + dc] <= 0:
                tmp_r_c_list.append((row + dr, col + dc))
    counter = Counter(tmp_r_c_list)

    if counter:
        # 친구 제일 많은 것
        max_count = counter.most_common(1)[0][1]
        max_count_r_c_list = []
        for curr, count in counter.items():
            if count == max_count:
                max_count_r_c_list.append([empty_count_map[curr[0]][curr[1]], curr])

        # 빈칸 많은 순, row, col
        _, (row, col) = sorted(max_count_r_c_list, key=lambda x: (x[0], x[1]))[0]
        count = -1 * empty_count_map[row][col]
        empty_count_dict[count].remove((row, col))
        heapq.heapify(empty_count_dict[count])
        fav_friends_count[row][col] = max_count

    else:
        # 친구 주변 빈자리 없을 때
        row, col = get_max_empty_count()
        fav_friends_count[row][col] = 0

    return row, col


def update_empty_count_map(student_id, row, col):
    """
    빈칸 수 map
        들어가는 칸 = -1
        그 주위 -= 1
        그 주위 칸 fav count 체크 후 추가

    빈칸 dict
        그 주위 칸: count -> count - 1 (if count > 0)
    """
    empty_count_map[row][col] = student_id

    for dr, dc in surround_dr_dc:
        if 0 <= row + dr < N and 0 <= col + dc < N:
            empty_count = empty_count_map[row + dr][col + dc]

            # 주변 친구 기준 현재 친구가 좋아하는 친구라면 += 1
            if empty_count_map[row + dr][col + dc] > 0:
                if student_id in student_fav_dict[empty_count]:
                    fav_friends_count[row + dr][col + dc] += 1
            # 빈칸 수 줄이기
            else:
                empty_count_dict[-1 * empty_count].remove((row + dr, col + dc))
                heapq.heapify(empty_count_dict[-1 * empty_count])
                if empty_count < 0:
                    heapq.heappush(empty_count_dict[-1 * empty_count - 1], (row + dr, col + dc))
                empty_count_map[row + dr][col + dc] += 1


# 들어간 학생 정보
student_info_dict = {}
# 학생 - 좋아하는 학생 정보
student_fav_dict = {}
# 학생 넣기
# s_id: 넣을 학생, *s_list: s_id 학생이 좋아하는 학생 리스트
for _ in range(N ** 2):
    s_id, *s_list = list(map(int, sys.stdin.readline().split()))
    student_fav_dict[s_id] = s_list

    # map에 매핑되어 있는 친구 위치 찾기
    fav_stu_rc_list = []
    for stu in s_list:
        if student_info_dict.get(stu) is not None:
            fav_stu_rc_list.append(student_info_dict[stu])

    # 좋아하는 학생 모두 map에 없음
    if len(fav_stu_rc_list) == 0:
        r, c = get_max_empty_count()

    # 좋아하는 학생 중 map에 있는 학생 있음
    else:
        r, c = find_most_common(fav_stu_rc_list)

    # 빈칸 수 정보 map에 업데이트
    update_empty_count_map(s_id, r, c)
    student_info_dict[s_id] = (r, c)

    print_map(empty_count_map)
    print()
    print_map(fav_friends_count)
    print(student_info_dict)

score = 0
score_dict = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
for i in range(N):
    for j in range(N):
        score += score_dict[fav_friends_count[i][j]]
print(score)
