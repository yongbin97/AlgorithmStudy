import sys
import time
from collections import deque
from typing import Optional, List

sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/포탑부수기/test1.txt", "r")
T = int(sys.stdin.readline())
dx_list = [0, 1, 0, -1]
dy_list = [1, 0, -1, 0]

for _ in range(T):
    # set data
    row, col, round_num = map(int, sys.stdin.readline().split())
    turret = []
    for _ in range(row):
        turret.append([[power, 0] for power in list(map(int, sys.stdin.readline().split()))])


    def get_turret(get_attacker: bool, attacker=None, round_num: int = None) -> Optional[List[int]]:
        """
        Step1 공격자 선정 및 Step2 타겟 선정
        params:
            get_attacker:bool
                True = Step1 공격자
                False = Step2 타겟
            round: 현재 라운드
            attacker: 선정된 공격자
        return:
            row, col
        """

        # turrets = [row, col, power, last_attack]
        turrets = []
        for i in range(row):
            for j in range(col):
                # 공격력 0 이하, 공격자 제외
                if turret[i][j][0] > 0 and [i, j] != attacker:
                    turrets.append([i, j, turret[i][j][0], turret[i][j][1]])

        if get_attacker:
            if len(turrets) == 1:
                return None
            attacker = sorted(turrets, key=lambda x: (x[2], -x[3], -(x[0] + x[1]), -x[1]))[0][:2]
            turret[attacker[0]][attacker[1]][0] += col + row
            turret[attacker[0]][attacker[1]][1] = round_num
            return attacker
        else:
            return sorted(turrets, key=lambda x: (-x[2], x[3], (x[0] + x[1]), x[1]))[0][:2]


    def attack_laser(attacker: List[int], target: List[int]) -> Optional[List[List[int]]]:
        """
        Step 2 공격 - 레이저 공격
        params:
            attacker
            target
        return:
            turrets: 공격 범위에 있는 포탑
        """
        dq = deque()
        dq.append([attacker, [attacker]])
        visited = [[attacker]]

        while dq:
            curr, path = dq.popleft()

            if curr == target:
                break

            for dx, dy in zip(dx_list, dy_list):
                next_x, next_y = (curr[0] + dx) % row, (curr[1] + dy) % col
                if turret[next_x][next_y][0] > 0 and [next_x, next_y] not in visited:
                    visited.append([next_x, next_y])
                    dq.append([[next_x, next_y], path + [[next_x, next_y]]])

        if target not in path:
            return None
        return path


    def attack_bomb(attacker: List[int], target: List[int]):
        """
        Step2 - 포탄 공격
        params:
            attacker
            target
        return:
            turrets: 공격 범위에 있는 포탑
        """
        turrets = [attacker]
        for dx in [1, -1, 0]:
            for dy in [1, -1, 0]:
                x, y = (target[0] + dx) % row, (target[1] + dy) % col
                if turret[x][y][0] > 0:
                    turrets.append([x, y])
        return turrets


    def damage(attacker, target, turrets) -> [List[List[int]]]:
        """
        공격 범위에 있는 포탑들 데미지 계산
        param:
            attacker: 공격 포탑
            target: 타겟 포탑
            turrets: 공격 범위에 있는 포탑들
        """
        if turrets:
            for t in turrets:
                if t == attacker:
                    continue
                elif t == target:
                    turret[t[0]][t[1]][0] -= turret[attacker[0]][attacker[1]][0]
                else:
                    turret[t[0]][t[1]][0] -= turret[attacker[0]][attacker[1]][0] // 2


    def attack(attacker: List[int]) -> List[List[int]]:
        """
        Step 2 공격
        레이저 -> 포탄 공격
        params:
            attacker
        return:
            turrets: 공격자, 타겟, 데미지 받은 포탑들
        """
        target = get_turret(get_attacker=False, attacker=attacker)
        turrets = attack_laser(attacker, target)
        if turrets is None:
            turrets = attack_bomb(attacker=attacker, target=target)
        damage(attacker, target, turrets)
        return turrets


    def increase_power(turrets: List[List[int]]):
        """
        Step 4 포탑 정비
        :param turrets:
        :return:
        """
        for i in range(row):
            for j in range(col):
                if turret[i][j][0] > 0 and [i, j] not in turrets:
                    turret[i][j][0] += 1


    # 진행
    start = time.time()
    for num in range(1, round_num + 1):
        attacker = get_turret(get_attacker=True, round_num=num)
        if attacker is None:
            break
        turrets = attack(attacker)
        increase_power(turrets)

    answer = 0
    for i in range(row):
        answer = max(answer, max(turret[i], key=lambda x: x[0])[0])
    print(answer)
    print(time.time() - start)
