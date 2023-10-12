import sys

sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/술래잡기/input.txt", "r")


def print_map(graph):
    for i in range(len(graph)):
        print(graph[i])


class Runner:
    def __init__(self, id, r, c, d):
        self.id = id
        self.r = r
        self.c = c
        self.d = d

    def get_next(self):
        return self.r + self.d[0], self.c + self.d[1]

    def change_dir(self):
        self.d = (self.d[0] * -1, self.d[1] * -1)

    def __repr__(self):
        return f"도망자{self.id}"


class Catcher:
    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d
        self.flag = True

    def move(self):
        self.r += self.d[0]
        self.c += self.d[1]
        return self.r, self.c

    def __repr__(self):
        return f"술래 ({self.r}, {self.c}), 방향: {self.d}"


n, m, h, k = map(int, sys.stdin.readline().split())

# 술래 방향 바꾸는 좌표
change_direction = [(0, 0), (n // 2, n // 2)]
# 도망자 {runner_id: Runner}
runner_dict = {}

# 도망자 지도
# TODO: runner list에 넣어서 보관하기
runner_map = []
for _ in range(n):
    row = []
    for _ in range(n):
        row.append([])
    runner_map.append(row)

# 나무 지도
tree_map = [[0] * n for _ in range(n)]
# 점수
score = 0

# 술래 방향 바꾸는 좌표 설정
for i in range(n // 2):
    change_direction.append((max(n // 2 - i - 1, 0), n // 2 - i))
    change_direction.append((n // 2 - i - 1, n // 2 + i + 1))
    change_direction.append((n // 2 + i + 1, n // 2 + i + 1))
    change_direction.append((n // 2 + i + 1, n // 2 - i - 1))

for i in range(m):
    x, y, d = map(int, sys.stdin.readline().split())
    if d == 1:
        d = (0, 1)
    else:
        d = (1, 0)
    runner_dict[i + 1] = Runner(i + 1, x - 1, y - 1, d)
    runner_map[x - 1][y - 1].append(i + 1)
for _ in range(h):
    x, y = map(int, sys.stdin.readline().split())
    tree_map[x - 1][y - 1] = -1

catcher = Catcher(n // 2, n // 2, (-1, 0))

print("runner")
print_map(runner_map)


def move_runner():
    """
    상하, 좌우로만 이동

    [이동 조건]
    술래와 간격이 3 이하만 이동
    다음 칸 : 격자 내부
    - 다음 칸에 술래가 있으면 움직이지 않음
    - 술래 없으면 이동 (나무 상관X)
    다음 칸 : 격자 외부
    - 방향 바꾸기 -> 술래 없으면 1칸 이동
    """
    for rid, runner in runner_dict.items():
        if abs(catcher.r - runner.r) + abs(catcher.c - runner.c) <= 3:
            next_r, next_c = runner.get_next()
            if not (0 <= next_r < n and 0 <= next_c < n):
                runner.change_dir()
                next_r, next_c = runner.get_next()
            if (next_r, next_c) != (catcher.r, catcher.c):
                # print(f"{runner}: ({runner.r}, {runner.c}) -> ({next_r}, {next_c})")
                runner_map[runner.r][runner.c].remove(runner.id)
                runner.r, runner.c = next_r, next_c
                runner_map[runner.r][runner.c].append(runner.id)


def move_catcher():
    """
    달팽이 모양으로 이동

    1. 1칸 이동
    2. 방향 바꾸는 지점 -> 방향 바꾸기
    """
    a, b = catcher.r, catcher.c
    r, c = catcher.move()
    print(f"술래: ({a}, {b}) -> ({catcher.r}, {catcher.c}) ")
    if (r, c) in change_direction:
        if r < n // 2:
            # 안 -> 밖: 우 -> 하
            # 밖 -> 안: 상 -> 좌
            if c > n // 2:
                catcher.d = (1, 0) if catcher.flag else (0, -1)
                print("술래 방향전환: 우 -> 하")
            # 안 -> 밖: 상 -> 우
            # 밖 -> 안: 좌 -> 하
            else:
                catcher.d = (0, 1) if catcher.flag else (1, 0)
                print("술래 방향전환: 상 -> 우")
        else:
            # 안 -> 밖: 하 -> 좌
            # 밖 -> 안: 우 -> 상
            if c >= n // 2:
                catcher.d = (0, -1) if catcher.flag else (-1, 0)
                print("술래 방향전환: 하 -> 좌")
            # 안 -> 밖: 좌 -> 상
            # 밖 -> 안: 하 -> 우
            else:
                catcher.d = (-1, 0) if catcher.flag else (0, 1)
                print("술래 방향전환: 좌 -> 상")


def catch(t, score):
    """
    술래 위치부터 바라보는 방향으로 3칸 (1,2) + 우측 => (1,2), (1,3), (1,4)
    나무 뒤는 못 잡음
    t 턴 -> t * 잡은 도망자 수 만큼 점수 획득

    잡힌 도망자 제거
    """
    r, c = catcher.r, catcher.c
    catch_runner = []
    for i in range(3):
        watch_r, watch_c = r + catcher.d[0] * i, c + catcher.d[1] * i
        if 0 <= watch_r < n and 0 <= watch_c < n:
            print(f"술래가 ({watch_r}, {watch_c}) 확인합니다.")
            if tree_map[watch_r][watch_c] == 0 and runner_map[watch_r][watch_c]:
                runner_id_list = runner_map[watch_r][watch_c]
                for runner_id in runner_id_list:
                    catch_runner.append(runner_dict[runner_id])

    for runner in catch_runner:
        print(f"{runner}가 잡혔습니다. {len(catch_runner) * t}점을 획득합니다.")
        runner_map[runner.r][runner.c].remove(runner.id)
        del runner_dict[runner.id]

    return score + len(catch_runner) * t


def rotate():
    if catcher.r == 0 and catcher.c == 0:
        catcher.d = (1, 0)
        catcher.flag = False

    if catcher.r == n // 2 and catcher.c == n // 2:
        catcher.d = (-1, 0)
        catcher.flag = True


t = 1
score = 0
while runner_dict and t <= k:
    print(t)
    move_runner()
    move_catcher()
    score = catch(t, score)
    rotate()
    t += 1
print(score)
