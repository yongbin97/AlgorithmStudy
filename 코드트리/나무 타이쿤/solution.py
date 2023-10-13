import sys

sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/나무 타이쿤/input.txt", "r")


def print_map(_map):
    for r in _map:
        print(r)


n, m = map(int, sys.stdin.readline().split())

# 나무 높이 정보 지도
tree_map = []
# 높이 2 이상 나무 정보
tree_over_2 = set()
# 각 연도별 이동 규칙
move_list = []
# 영양제
m_list = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

# 방향 dict
direction = {0: (0, 1), 1: (-1, 1), 2: (-1, 0), 3: (-1, -1), 4: (0, -1), 5: (1, -1), 6: (1, 0), 7: (1, 1)}

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j, h in enumerate(row):
        if h >= 2:
            tree_over_2.add((i, j))
    tree_map.append(row)

for _ in range(m):
    d, p = list(map(int, sys.stdin.readline().split()))
    move_list.append([d - 1, p])


def move_m(d_i, num):
    m_map = [[0] * n for _ in range(n)]

    for m_i in range(len(m_list)):
        r, c = m_list[m_i]
        dr, dc = direction[d_i]
        m_list[m_i] = [(r + dr * num) % n, (c + dc * num) % n]
        m_map[(r + dr * num) % n][(c + dc * num) % n] = 1
    return m_map


def growth(m_map):
    while m_list:
        r, c = m_list.pop()
        tree_map[r][c] += 1
        extra_h = 0
        for i in range(4):
            dr, dc = direction[2 * i + 1]
            if 0 <= r + dr < n and 0 <= c + dc < n:
                if tree_map[r + dr][c + dc] >= 1 or m_map[r + dr][c + dc] == 1:
                    extra_h += 1
        tree_map[r][c] += extra_h
        if tree_map[r][c] >= 2:
            tree_over_2.add((r, c))


def new_m(m_map):
    for r in range(n):
        for c in range(n):
            if tree_map[r][c] >= 2 and m_map[r][c] == 0:
                tree_map[r][c] -= 2
                m_list.append([r, c])


for d, p in move_list:
    # 이동 후 영양제 위치 기록
    med_map = move_m(d, p)
    growth(med_map)
    new_m(med_map)

h_sum = 0
for row in tree_map:
    h_sum += sum(row)
print(h_sum)
