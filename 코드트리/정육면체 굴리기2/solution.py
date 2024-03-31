import sys

# sys.stdin = open("input.txt", "r")


# def print_arr(arr):
#     for r in range(len(arr)):
#         for c in range(len(arr[0])):
#             print(arr[r][c], end="\t")
#         print()
#     print()


# n = 말판 세로 길이
# m = 말판 가로 길이
# r, c = 주사위 초기 위치
# k = 굴리는 횟수
n, m, r, c, k = map(int, sys.stdin.readline().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

command_list = list(map(int, sys.stdin.readline().split()))

# x1, x2, y1, y2, z1, z2
dice = [0, 0, 0, 0, 0, 0]


def rotate_dice(command):
    # 동
    if command == 1:
        y1, y2, z1, z2 = dice[2:]
        dice[2] = z1
        dice[3] = z2
        dice[4] = y2
        dice[5] = y1

    # 서
    elif command == 2:
        y1, y2, z1, z2 = dice[2:]
        dice[2] = z2
        dice[3] = z1
        dice[4] = y1
        dice[5] = y2

    # 북
    elif command == 3:
        x1, x2, z1, z2 = dice[:2] + dice[4:]
        dice[0] = z2
        dice[1] = z1
        dice[4] = x1
        dice[5] = x2

    # 남
    else:
        x1, x2, z1, z2 = dice[:2] + dice[4:]
        dice[0] = z1
        dice[1] = z2
        dice[4] = x2
        dice[5] = x1


def is_possible(command):
    global r, c, n, m

    # 동
    if command == 1 and 0 <= c + 1 < m:
        c += 1
        return True

    # 서
    elif command == 2 and 0 <= c - 1 < m:
        c -= 1
        return True
    # 북
    elif command == 3 and 0 <= r - 1 < n:
        r -= 1
        return True
    # 남
    elif command == 4 and 0 <= r + 1 < n:
        r += 1
        return True

    return False


for command in command_list:
    # print(f"COMMAND: {command}")
    if is_possible(command):
        rotate_dice(command)

        if maps[r][c] == 0:
            maps[r][c] = dice[5]
        else:
            dice[5] = maps[r][c]
            maps[r][c] = 0
        print(dice[4])




