import sys
from collections import deque, defaultdict


class ColorGroup:
    def __init__(self, color, size, rainbow_count, min_block, block_list):
        self.color = color
        self.size = size
        self.rainbow_count = rainbow_count
        self.min_block = min_block
        self.block_list = block_list

    def __lt__(self, other):
        if self.size != other.size:
            return self.size < other.size
        if self.rainbow_count != other.rainbow_count:
            return self.rainbow_count < other.rainbow_count
        return self.min_block < other.min_block


N, M = map(int, sys.stdin.readline().split())

# 블록 맵
blocks_map = []
for _ in range(N):
    blocks_map.append(list(map(int, sys.stdin.readline().split())))


def rotate():
    """
    blocks_map -90도 회전
    """
    global blocks_map
    new_block_map = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_block_map[N - 1 - j][i] = blocks_map[i][j]

    blocks_map = new_block_map


def search_bfs(r, c, visited):
    dr_list = [1, -1, 0, 0]
    dc_list = [0, 0, 1, -1]
    local_visited = [[False] * N for _ in range(N)]
    color_num = blocks_map[r][c]

    rainbow_count = 0
    min_block = (r, c)
    group_list = [(r, c)]
    local_visited[r][c] = True

    dq = deque()
    dq.append([r, c])
    while dq:
        r, c = dq.popleft()
        for dr, dc in zip(dr_list, dc_list):
            next_r, next_c = r + dr, c + dc

            if (
                0 <= next_r < N and 0 <= next_c < N
                and blocks_map[next_r][next_c] in [0, color_num]
                and not local_visited[next_r][next_c]
            ):
                dq.append([next_r, next_c])
                group_list.append((next_r, next_c))
                local_visited[next_r][next_c] = True

                if blocks_map[next_r][next_c] == 0:
                    rainbow_count += 1
                else:
                    visited[next_r][next_c] = True
                    min_block = min(min_block, (next_r, next_c))

    return group_list, rainbow_count, min_block, visited


def find_group():
    # {color_id: ColorGroup}
    color_group = {}
    # 무지개, -1 제외 방문 여부
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and blocks_map[i][j] != "#" and blocks_map[i][j] > 0:
                color_id = blocks_map[i][j]
                group_list, rainbow_count, min_block, visited = search_bfs(i, j, visited)
                if len(group_list) >= 2:
                    if color_group.get(color_id) is None:
                        # color, size, rainbow_count, min_block, block_list
                        color_group[color_id] = ColorGroup(color_id, len(group_list), rainbow_count, min_block, group_list)
                    else:
                        new_group = ColorGroup(color_id, len(group_list), rainbow_count, min_block, group_list)
                        if new_group > color_group[color_id]:
                            color_group[color_id] = new_group

    if color_group:
        max_color_id = sorted(color_group.items(), key=lambda x: x[1], reverse=True)[0][0]
        return color_group[max_color_id].block_list
    else:
        return None


def gravity():
    stack = [deque() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if blocks_map[i][j] == "#":
                stack[j].appendleft(blocks_map[i][j])
            elif blocks_map[i][j] >= 0:
                stack[j].append(blocks_map[i][j])
            else:
                for k in range(i-1, -1, -1):
                    if blocks_map[k][j] == -1:
                        break
                    if stack[j]:
                        blocks_map[k][j] = stack[j].pop()
                    else:
                        blocks_map[k][j] = "#"

    for j, st in enumerate(stack):
        if st:
            for k in range(N - 1, -1, -1):
                if blocks_map[k][j] == -1:
                    break
                blocks_map[k][j] = stack[j].pop()




def remove_blocks(block_list):
    for r, c in block_list:
        blocks_map[r][c] = "#"


score = 0
idx = 1
while True:
    block_group = find_group()
    if block_group is None:
        break
    score += len(block_group) ** 2
    remove_blocks(block_group)
    gravity()
    rotate()
    gravity()
    idx += 1
print(score)