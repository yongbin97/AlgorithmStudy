import sys


class Knight:
    def __init__(self, r, c, h, w, k):
        self.r = r
        self.c = c
        self.h = h
        self.w = w
        self.k = k
        self.damage = 0

    def move_knight(self, dir_id):
        dir_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        dr, dc = dir_list[dir_id]
        self.r += dr
        self.c += dc

    def get_damage(self):
        for row in range(self.r, self.r + self.h):
            for col in range(self.c, self.c + self.w):
                if graph[row][col] == 1:
                    self.k -= 1
                    self.damage += 1


# L: 체스판 크기, N: 기사의 수, Q: 명령의 수
L, N, Q = map(int, sys.stdin.readline().split())

graph = []
for _ in range(L):
    graph.append(list(map(int, sys.stdin.readline().split())))

knight_graph = [[0] * L for _ in range(L)]
knight_dict = {}
for idx in range(N):
    r, c, h, w, k = map(int, sys.stdin.readline().split())
    knight_dict[idx + 1] = Knight(r - 1, c - 1, h, w, k)

    for row in range(r - 1, r + h - 1):
        for col in range(c - 1, c + w - 1):
            knight_graph[row][col] = idx + 1


def move_knight(knight_id, dir_id):
    knight = knight_dict[knight_id]

    if dir_id % 2 == 0:
        for col in range(knight.c, knight.c + knight.w):
            # 상
            if dir_id == 0:
                knight_graph[knight.r + knight.h - 1][col] = 0
                knight_graph[knight.r - 1][col] = knight_id
            # 하
            else:
                knight_graph[knight.r + knight.h][col] = knight_id
                knight_graph[knight.r][col] = 0
    else:
        for row in range(knight.r, knight.r + knight.h):
            # 우
            if dir_id == 1:
                knight_graph[row][knight.c] = 0
                knight_graph[row][knight.c + knight.w] = knight_id
            # 좌
            else:
                knight_graph[row][knight.c - 1] = knight_id
                knight_graph[row][knight.c + knight.w - 1] = 0

    knight.move_knight(dir_id)


def get_damage_knight(knight_id):
    knight = knight_dict[knight_id]
    knight.get_damage()
    if knight.k <= 0:
        remove_knight(knight_id)


def remove_knight(knight_id):
    knight = knight_dict[knight_id]

    for row in range(knight.r, knight.r + knight.h):
        for col in range(knight.c, knight.c + knight.w):
            knight_graph[row][col] = 0

    del knight_dict[knight_id]


def search(knight_id, dir_id, visited_knight):
    """
    DFS를 응용한 풀이
    마지막 노드까지 탐색하면서 이동이 가능한지 확인
    """
    knight = knight_dict[knight_id]
    next_knight_list = []

    def set_next_knight_list():
        # 벽
        if (
                not (0 <= row < L and 0 <= col < L)
                or graph[row][col] == 2
        ):
            return False

        # 다음 기사 탐색
        elif (
                knight_graph[row][col] != 0
                and knight_graph[row][col] not in next_knight_list
                and knight_graph[row][col] not in visited_knight
        ):
            next_knight_list.append(knight_graph[row][col])

    # 상, 하
    if dir_id % 2 == 0:
        row = knight.r - 1 if dir_id == 0 else knight.r + knight.h
        for col in range(knight.c, knight.c + knight.w):
            if set_next_knight_list() is False:
                return None

    # 좌, 우
    else:
        col = knight.c - 1 if dir_id == 3 else knight.c + knight.w
        for row in range(knight.r, knight.r + knight.h):
            if set_next_knight_list() is False:
                return None

    # 다음 기사 있는 경우
    if next_knight_list:
        knight_list = []
        for next_knight_id in next_knight_list:
            knight_id_list = search(next_knight_id, dir_id, visited_knight + [next_knight_id])
            if knight_id_list is None:
                return None
            knight_list += knight_id_list

        return knight_list + [knight_id]

    return [knight_id]


# main
for i in range(Q):
    start_knight_id, dir_id = map(int, sys.stdin.readline().split())
    if start_knight_id not in knight_dict.keys():
        continue
    visited_knight = []
    knight_list = search(start_knight_id, dir_id, visited_knight)

    # 이동
    if knight_list is not None:
        for knight_id in knight_list:
            move_knight(knight_id, dir_id)
            if knight_id != start_knight_id:
                get_damage_knight(knight_id)


answer = 0
for knight in knight_dict.values():
    answer += knight.damage
print(answer)