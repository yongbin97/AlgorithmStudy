import sys
import copy


class Runner:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return f"[{self.row}, {self.col}]"


sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/메이즈러너/input.txt", "r")
N, M, K = map(int, sys.stdin.readline().split())
maze = []
runners = []

for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().split())))
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    runners.append(Runner(i - 1, j - 1))

r, c = map(int, sys.stdin.readline().split())
exit_maze = [r - 1, c - 1]


def get_distance(curr_r, curr_c):
    return abs(curr_r - exit_maze[0]) + abs(curr_c - exit_maze[1])


def set_square():
    """
    return: [[좌상단 좌표], 변의 길이]
    """
    small_square = [N, [N, N]]
    for runner in runners:
        if runner.row == exit_maze[0]:
            dist = abs(runner.col - exit_maze[1])
            corner = [max(runner.row - dist, 0), min(runner.col, exit_maze[1])]

        elif runner.col == exit_maze[1]:
            dist = abs(runner.row - exit_maze[0])
            corner = [min(runner.row, exit_maze[0]), max(runner.col - dist, 0)]

        else:
            dist = max(abs(runner.col - exit_maze[1]), abs(runner.row - exit_maze[0]))
            corner = [max(max(runner.row, exit_maze[0]) - dist, 0), max(max(runner.col, exit_maze[1]) - dist, 0)]

        small_square = min(small_square, [dist + 1, corner])
    return small_square


def rotate(square, a, b):
    """
    square: [변의 길이, [좌상단 row, col]]
    square 기준으로 r, c rotate

    a,b => b + row - col, 변의 길이 - 1 - a + row + col

    return new_r, new_c
    """
    dist, [row, col] = square
    return b + row - col, dist - 1 - a + row + col


def rotate_maze(square):
    """
    square: [변의 길이, [좌상단 row, col]]
    """
    dist, [row, col] = square
    original_maze = copy.deepcopy(maze)

    # rotate maze
    for x in range(row, row + dist):
        for y in range(col, col + dist):
            new_x, new_y = rotate(square, x, y)
            maze[new_x][new_y] = max(original_maze[x][y] - 1, 0)

    # rotate exit
    exit_maze[0], exit_maze[1] = rotate(square, exit_maze[0], exit_maze[1])

    # rotate runner
    for runner in runners:
        if row <= runner.row < row + dist and col <= runner.col < col + dist:
            runner.row, runner.col = rotate(square, runner.row, runner.col)

    # heapq.heapify(runners)


def run(running_count):
    exit_runners = []
    for runner in runners:
        dx_list = [-1, 1, 0, 0]
        dy_list = [0, 0, -1, 1]
        curr_distance = get_distance(runner.row, runner.col)

        # 이동
        for dx, dy in zip(dx_list, dy_list):
            next_row, next_col = runner.row + dx, runner.col + dy
            if 0 <= next_row < N and 0 <= next_col < N and maze[next_row][next_col] == 0:
                if get_distance(next_row, next_col) < curr_distance:
                    print(f"run: {runner} -> [{next_row}, {next_col}]")
                    runner.row, runner.col = next_row, next_col
                    running_count += 1
                    break
        # 탈출
        if [runner.row, runner.col] == exit_maze:
            exit_runners.append(runner)

    for exit_runner in exit_runners:
        runners.remove(exit_runner)
    return running_count


def print_maze():
    for i in range(N):
        print(f"{i}: {maze[i]}")


print_maze()
running_count = 0
for i in range(K):
    print(f"round:{i + 1}, exit:{exit_maze}, runner:{runners}, running_count:{running_count}")

    running_count = run(running_count)
    if len(runners) == 0:
        break
    square = set_square()
    print(square)
    rotate_maze(square)

    print_maze()
    print(f"round:{i + 1} done, exit:{exit_maze}, runner:{runners}, running_count:{running_count}")
    print()

print(running_count)
print(f"{exit_maze[0] + 1} {exit_maze[1] + 1}")
exit_maze[0] += 1
exit_maze[1] += 1

print(running_count, exit_maze)

# def compare(runner1, runner2):
#     l1 = abs(runner1.row - exit_maze[0]) + abs(runner1.col - exit_maze[1])
#     l2 = abs(runner2.row - exit_maze[0]) + abs(runner2.col - exit_maze[1])
#     return l1 < l2


# def __lt__(self, other):
#     return compare(self, other)


# def get_closest_runners():
#     closest_runners = []
#     d = 2 * N
#     while runners:
#         runner = heapq.heappop(runners)
#         if get_distance(runner.row, runner.col) <= d:
#             closest_runners.append(runner)
#             d = get_distance(runner.row, runner.col)
#         else:
#             heapq.heappush(runners, runner)
#             break
#     for runner in closest_runners:
#         heapq.heappush(runners, runner)
#     return closest_runners
