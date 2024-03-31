import sys


# n: row, m: col
n, m = map(int, sys.stdin.readline().split())
# x, y : 자동차 초기 위치
# dir_dix: 최초 방향
x, y, dir_idx = map(int, sys.stdin.readline().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

visited = [[False] * m for _ in range(n)]

# 북 동 남 서
dir_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 1


def move(count, r, c, dir_idx):
    """
    count: 현재 자리에서 회전한 횟수
    r, c 현재 위치
    """
    # 현재 자리에서 4 방향 모두 확인
    if count == 4:
        dr, dc = dir_list[dir_idx]
        next_r, next_c = r + -1 * dr, c + -1 * dc

        # 후진
        if maps[next_r][next_c] == 0:
            # print(f"후진: {r, c} -> {next_r, next_c}")
            return 0, next_r, next_c, dir_idx

        else:
            # print("종료")
            return -1, -1, -1, -1

    dr, dc = dir_list[(dir_idx - 1) % 4]
    next_r, next_c = r + dr, c + dc

    # 좌회전 후 1칸 전진
    if maps[next_r][next_c] == 0 and not visited[next_r][next_c]:
        # print(f"좌회전 후 1칸 전진 {r, c} -> {next_r, next_c}")
        global answer
        answer += 1
        visited[next_r][next_c] = True
        return 0, next_r, next_c, (dir_idx - 1) % 4

    # 자회전
    else:
        # print(f"자회전 {r, c}")
        return count + 1, r, c, (dir_idx - 1) % 4


count = 0
visited[x][y] = True
while True:
    count, x, y, dir_idx = move(count, x, y, dir_idx)
    if dir_idx == -1:
        break

print(answer)
