import sys
from collections import deque

sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/코드트리 빵/test.txt", "r")
n, m = map(int, sys.stdin.readline().split())
maps = []

# i: [a, b] -> i 번째 사람 목표 편의점 (a,b)
store_dict = {}
# i: [x, y] -> i 번째 사람 현재 위치 (x,y)
people_dict = {}
# i: [[], []] -> i 번째 사람 현재 위치부터 목표 편의점까지 최단 경로
path_dict = {}

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().split())
    store_dict[i] = (a - 1, b - 1)


def print_maps():
    for i in range(n):
        print(f"{i}: {maps[i]}")


print_maps()
print(store_dict)


def search_basecamp():
    """
    i번째 사람 목표 편의점 기준으로 가장 가까운 베이스 캠프 찾기
    상, 좌, 우, 하 순으로 이동 (우선순위: col, row)

    path_dict[i] = path[::-1]
    people_dict[i] = [base_r, base_c]
    maps[base_r][base_c] != -1
    """
    visited = [[False] * n for _ in range(n)]
    dx_list = [-1, 0, 0, 1]
    dy_list = [0, -1, 1, 0]

    store = store_dict[idx]
    dq = deque()
    path = [store]
    dq.append([*store, path])
    while dq:
        x, y, path = dq.popleft()

        # end: base_camp
        if maps[x][y] == 1:
            break

        for dx, dy in zip(dx_list, dy_list):
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
                if maps[new_x][new_y] != -1:
                    dq.append([new_x, new_y, [(new_x, new_y)] + path])
                    visited[new_x][new_y] = True

    path_dict[idx] = deque(path[1:])
    people_dict[idx] = (x, y)
    maps[x][y] = -1
    return x, y


def search_shortest_path(pid):
    """
    현재 위치로부터 편의점까지 가장 가까운 길 찾기
    (상, 좌, 우, 하) 순으로 이동
    path_dict[i] = path
    """
    visited = [[False] * n for _ in range(n)]
    dx_list = [-1, 0, 0, 1]
    dy_list = [0, -1, 1, 0]

    curr = people_dict[pid]
    dq = deque()
    path = [curr]
    dq.append([*curr, path])
    while dq:
        x, y, path = dq.popleft()

        # end: store
        if (x, y) == store_dict[pid]:
            break

        for dx, dy in zip(dx_list, dy_list):
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
                if maps[new_x][new_y] != -1:
                    dq.append([new_x, new_y, path + [(new_x, new_y)]])
                    visited[new_x][new_y] = True

    path_dict[pid] = deque(path[1:])
    print(f"{pid} new path: {path[1:]}")


def find_path_with_disabled_path(x, y):
    for pid, path in path_dict.items():
        if path is not None and (x, y) in path:
            print(f"pid:{pid}, path_dict[pid]=None")
            path_dict[pid] = None


def move():
    """
    step 1
    최단 거리로 (상, 좌, 우, 하) 1칸 이동
    if path_dict[i] is None:
        search_shortest_path
    else:
        move
    """
    for pid, curr in people_dict.items():
        if path_dict[pid] is None:
            search_shortest_path(pid)

        people_dict[pid] = path_dict[pid].popleft()


def end():
    """
    step 2
    목표 편의점 도착
    - 이동 못하는 지역으로 선정
    - 해당 사람 disabled maps[r][c] = -1
    - 현재 위치를 최소 경로에 가지고 있는 사람 경로 삭제
    """
    arrived_people = []
    for pid, (r, c) in people_dict.items():
        if (r, c) == store_dict[pid]:
            maps[r][c] = -1
            arrived_people.append(pid)
            find_path_with_disabled_path(r, c)

    for pid in arrived_people:
        del people_dict[pid]
        del path_dict[pid]
        del store_dict[pid]


def start():
    """
    step 3
    목표 편의점 기준 가장 가까운 베이스 캠프로 이동
    최단 경로 저장
    people_dict[i] = [base_r, base_c]
    path_dict[i] = path
    """
    if idx <= m:
        base_r, base_c = search_basecamp()
        print(f"{idx} base camp: ({base_r}, {base_c})")
        find_path_with_disabled_path(base_r, base_c)

disabled_list = []
idx = 1
while store_dict:
    print(f"########MIN: {idx}################")
    print(f"people_dict: {people_dict}")
    print(f"path_dict: {path_dict}")
    move()
    end()
    start()
    idx += 1
    print(f"[RESULT]")
    print(f"people_dict: {people_dict}")
    print(f"path_dict: {path_dict}")

print(idx-1)
