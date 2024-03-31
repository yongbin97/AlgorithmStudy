import sys

n, m = map(int, sys.stdin.readline().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

except_list = []


def search(level, r, c, visited):
    # 종료 조건
    if level == 4:
        return maps[r][c]

    curr_max = 0
    for r, c in visited:
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            next_r, next_c = r + dr, c + dc
            if (
                    0 <= next_r < n and 0 <= next_c < m
                    and [next_r, next_c] not in visited
            ):
                curr_max = max(curr_max, search(level + 1, next_r, next_c, visited + [[next_r, next_c]]))

    return curr_max + maps[r][c]


answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, search(1, i, j, [[i, j]]))

print(answer)
