import sys
import time

sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/팩맨/input.txt", "r")


def print_map(_map):
    for i in range(len(_map)):
        print(_map[i])


# 0: 상, 1:좌상, 2: 좌, 3: 좌하, 4: 하, 5: 우하, 6: 우, 7"우상
direction = {
    0: (-1, 0),
    1: (-1, -1),
    2: (0, -1),
    3: (1, -1),
    4: (1, 0),
    5: (1, 1),
    6: (0, 1),
    7: (-1, 1)
}


class Pacman:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __repr__(self):
        return f"팩맨 ({self.r}, {self.c})"


class Monster:
    """
    몬스터 위치 (r,c)
    id: monster id
    d: # of direciton
    """

    def __init__(self, id, r, c, d):
        self.id = id
        self.r = r
        self.c = c
        self.d = d

    def change_direction(self):
        self.d = (self.d + 1) % 8

    def get_next_step(self):
        dr, dc = direction[self.d]
        return self.r + dr, self.c + dc

    def __repr__(self):
        return f"몬스터{self.id}"


m, t = map(int, sys.stdin.readline().split())
pac_r, pac_c = map(int, sys.stdin.readline().split())
pacman = Pacman(pac_r - 1, pac_c - 1)

# 몬스터 정보 {m_id: Monster}
monster_dict = {}
# 몬스터 시체 정보 death_maps[i][j] = 없어지기 전까지 남은 라운드
death_maps = [[0] * 4 for _ in range(4)]
# 지도
maps = []
for _ in range(4):
    row = []
    for _ in range(4):
        row.append([])
    maps.append(row)

global m_id
m_id = 1
for _ in range(m):
    mon_r, mon_c, mon_d = map(int, sys.stdin.readline().split())
    monster_dict[m_id] = Monster(m_id, mon_r - 1, mon_c - 1, mon_d - 1)
    maps[mon_r - 1][mon_c - 1].append(m_id)
    m_id += 1


def copy_monster():
    """
    Step 1: 몬스터 복제 시도
    현재 위치에 자신과 같은 방향을 가진 몬스터
    알 상태: 이동 불가
    알 부화: 해당 방향으로 꺠어남
    """
    # 몬스터 알 정보 {m_id: Monster}:
    egg_dict = {}
    global m_id
    for _, monster in monster_dict.items():
        egg_dict[m_id] = Monster(m_id, monster.r, monster.c, monster.d)
        m_id += 1

    return egg_dict


def move_monster():
    """
    Step 2: 몬스터 이동
    자신의 방향대로 1칸 이동
    몬스타 시체가 있거나 팩맨이 있는 경우 격자를 벗어나는 방향
        -> 가능한 방향이 나올 때까지 방향성 반시계 방향으로 45도 회전
    * 한 칸에 몬스터 중복 가능
    """
    for id, monster in monster_dict.items():
        for _ in range(8):
            next_r, next_c = monster.get_next_step()
            if (
                    not (0 <= next_r < 4 and 0 <= next_c < 4)
                    or death_maps[next_r][next_c] < 0
                    or (pacman.r, pacman.c) == (next_r, next_c)
            ):
                monster.change_direction()
            else:
                maps[monster.r][monster.c].remove(monster.id)
                print(f"{monster} 이동: {monster.r, monster.c} -> {next_r, next_c}")
                monster.r, monster.c = next_r, next_c
                maps[monster.r][monster.c].append(monster.id)
                break


def kill_monster(monster_list):
    for mid in monster_list:
        death_monster = monster_dict[mid]
        print(f"{death_monster}이 잡혔습니다.")
        maps[death_monster.r][death_monster.c].remove(death_monster.id)
        death_maps[death_monster.r][death_monster.c] = -3
        del monster_dict[mid]
    print(f"monster:{monster_dict}")


def get_monster_id_set(r, c, monster_set):
    monset_id_set = set()
    for mid in maps[r][c]:
        if mid > 0 and mid not in monster_set:
            monset_id_set.add(mid)
    return monset_id_set.union(monster_set)


def move_pacman():
    """
    Step 3: 팩맨 이동
    총 3칸 이동
    각 이동마다 상하좌우 선택
    가장 몬스터를 많이 먹을 수 있는 방향으로 이동
        우선순위: 상 - 좌 - 하 - 우

    몬스터 만나면 먹어 치운 뒤 시체를 남김
    알 먹지 않음. 움직이기 전 같이 있는 몬스터 먹지 않음
    => 이동하는 과정에 있는 몬스터만 먹음
    """

    # 몬스터 중복 제거 예외처리
    def dfs(r, c, idx, path, monster_set):
        # action
        monster_set = get_monster_id_set(r, c, monster_set)

        # end
        if idx == 3:
            return [monster_set, path, (r, c)]

        # next
        tmp_result_list = []
        for p_i in range(4):
            dr, dc = direction[2 * p_i]
            next_r, next_c = r + dr, c + dc
            if 0 <= next_r < 4 and 0 <= next_c < 4:
                tmp_result_list.append(dfs(next_r, next_c, idx + 1, path + [p_i], monster_set))

        result = sorted(tmp_result_list, key=lambda x: (-(len(x[0])), x[1]))[0]
        return result

    result_list = []
    for d_idx in range(4):
        dr, dc = direction[2 * d_idx]
        next_r, next_c = pacman.r + dr, pacman.c + dc
        if 0 <= next_r < 4 and 0 <= next_c < 4:
            res = dfs(next_r, next_c, 1, [d_idx], set())
            result_list.append(res)

    result = sorted(result_list, key=lambda x: (-(len(x[0])), x[1]))[0]
    print(result)
    monster_id_list, _, (r, c) = result
    print(f"{pacman} 이동: ({pacman.r}, {pacman.c}) -> ({r}, {c})")
    pacman.r, pacman.c = r, c
    kill_monster(list(set(monster_id_list)))


def remove_monster():
    """
    Step 4: 시체 처리
    시체는 2턴동안 유지
    """
    for i in range(4):
        for j in range(4):
            if death_maps[i][j] < 0:
                death_maps[i][j] += 1
    print_map(death_maps)


def hatch_egg(egg_dict):
    """
    Step 5: 몬스터 복제 완료
    알이었던 몬스터 부화
    """
    for mid, monster in egg_dict.items():
        maps[monster.r][monster.c].append(mid)
        monster_dict[monster.id] = monster
        print(f"{monster}가 부화하였습니다.")


start = time.time()
step2 = 0
step3 = 0
step4 = 0
step5 = 0
for i in range(t):
    print(f"ROUND: {i}")
    egg_dict = copy_monster()
    start2 = time.time()
    move_monster()
    start3 = time.time()
    move_pacman()
    start4 = time.time()
    remove_monster()
    start5 = time.time()
    hatch_egg(egg_dict)
    end = time.time()
    step2 += start3-start2
    step3 += start4-start3
    step4 += start5-start4
    step5 += end-start5

print(len(monster_dict))
print(time.time()-start)
print(f"step2:{step2}")
print(f"step3:{step3}")
print(f"step4:{step4}")
print(f"step5:{step5}")