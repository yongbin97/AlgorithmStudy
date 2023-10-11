import sys
import heapq
from typing import Optional

# 총 정보가 있는 지도
gun_map = []
# 플레이어 위치 정보가 있는 지도
player_map = []
# 플레이어 리스트
players = []
# 플레이어 점수 리스트
player_score = []
# 방향 정보
direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}


class Player:
    def __init__(self, id, x, y, d, s):
        self.id = id
        self.x = x
        self.y = y
        self.d = d
        self.attk = s
        self.gun = 0

    def __lt__(self, other):
        if self.attk + self.gun != other.attk + other.gun:
            return self.attk + self.gun < other.attk + other.gun
        return self.attk < other.attk

    def __repr__(self):
        return f"p{self.id}"

    def __str__(self):
        return f"player{self.id} " \
               f"attk:{self.attk} " \
               f"gun:{self.gun} " \
               f"d:{self.d} " \
               f"curr: {self.x}, {self.y}"


sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/싸움땅/input.txt", "r")
n, m, k = map(int, sys.stdin.readline().split())
for _ in range(n):
    guns = list(map(int, sys.stdin.readline().split()))
    gun_map.append([[-1 * gun] for gun in guns])
player_map = [[0] * n for _ in range(n)]

for i in range(m):
    x, y, d, s = map(int, sys.stdin.readline().split())
    new_player = Player(i, x - 1, y - 1, d, s)
    players.append(new_player)
    player_map[x - 1][y - 1] = new_player
player_score = [0] * m


def print_map(_map):
    for i in range(len(_map)):
        print(_map[i])


def get_fight_score(player1: Player, player2: Player):
    score = abs((player1.attk + player1.gun) - (player2.attk + player2.gun))
    if player1 > player2:
        return player1, player2, score
    else:
        return player2, player1, score


def get_gun(player):
    """
    현재 칸의 총에서 가장 강한 총 획득, 나머지는 격자에 그대로
    """
    if gun_map[player.x][player.y]:
        if player.gun != 0:
            heapq.heappush(gun_map[player.x][player.y], -1 * player.gun)
        player.gun = -1 * heapq.heappop(gun_map[player.x][player.y])
        print(f"player{player.id}가 총({player.gun})을 얻었습니다. {gun_map[player.x][player.y]}")


def move(player: Player) -> Optional[Player]:
    """
    step 1

    player 현재 방향대로 이동
    격자에 닿으면 반대 방향
    """
    player_map[player.x][player.y] = 0
    direct = direction[player.d]
    # 방향 전환
    if not (0 <= player.x + direct[0] < n and 0 <= player.y + direct[1] < n):
        player.d = (player.d + 2) % 4

    direct = direction[player.d]
    next_x, next_y = player.x + direct[0], player.y + direct[1]

    print(f"player{player.id}가 ({player.x}, {player.y})에서 ({next_x}, {next_y})으로 이동합니다.")
    player.x, player.y = next_x, next_y

    # 움직일 칸에 상대 플레이어가 없는 경우
    if player_map[next_x][next_y] == 0:
        print(f"({player.x}, {player.y})에 플레이어가 없습니다.")
        player_map[next_x][next_y] = player
        get_gun(player)
        return None
    # 움직일 칸에 상대 플레이어가 있는 경우
    else:
        return player_map[next_x][next_y]


def win(player, score):
    """
    이긴 플레이어는 승리한 칸들의 총 + 자신의 총 중 가장 높은 공격력의 총 획득
    """
    player_score[player.id] += score
    player_map[player.x][player.y] = player
    get_gun(player)


def lose(player):
    """
    진 플레이어는 총을 내려놓고 원래 방향으로 한칸 이동
    만약 격자 밖 or 다른 플레이어가 있는 경우 오른쪽으로 90도 회전하다가 보이는 순간 이동
    이동 이후 총이 있다면 가장 높은 공격력의 총 획득
    """
    # drop gun
    if player.gun != 0:
        heapq.heappush(gun_map[player.x][player.y], -1 * player.gun)
    print(f"패배한 player{player.id}가 총({player.gun})을 내려놓았습니다. {gun_map[player.x][player.y]}")
    player.gun = 0

    # move
    for _ in range(4):
        direct = direction[player.d]
        next_x, next_y = player.x + direct[0], player.y + direct[1]
        if 0 <= next_x < n and 0 <= next_y < n and player_map[next_x][next_y] == 0:
            print(f"패배한 player{player.id}가 ({player.x}, {player.y}) -> ({next_x}, {next_y})로 이동합니다.")
            player.x, player.y = next_x, next_y
            player_map[next_x][next_y] = player
            break
        player.d = (player.d + 1) % 4
    # get new gun
    get_gun(player)


def fight(player, player2):
    """
    이긴 플레이어는 공격력 차이만큼 점수 획득
    """
    winner, loser, score = get_fight_score(player, player2)
    print(f"player{winner.id}가 player{loser.id}와 싸워 player{winner.id}가 이겼습니다. 점수 {score}를 획득합니다.")
    lose(loser)
    win(winner, score)


for player in players:
    print(player)

for i in range(k):
    print(f"#####ROUND: {i}#####")
    for curr_p in players:
        other_p = move(curr_p)
        if other_p is not None:
            fight(curr_p, other_p)

    for player in players:
        print(player)
    print()

print(" ".join([str(s) for s in player_score]))
