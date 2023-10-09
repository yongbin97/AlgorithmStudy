import sys
import time
from collections import deque
from typing import List, Optional


class Solution:
    def __init__(self):
        """
        입력 받은 포탑 정보 세팅
        turret = (power, last_attack_round)
        """
        self.row, self.col, self.round_num = map(int, sys.stdin.readline().split())
        self.turret = []
        for _ in range(self.row):
            self.turret.append([[power, 0] for power in list(map(int, sys.stdin.readline().split()))])

    def _get_turret(self, get_attacker: bool, attacker=None, round_num: int = None) -> Optional[List[int]]:
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
        for i in range(self.row):
            for j in range(self.col):
                # 공격력 0 이하, 공격자 제외
                if self.turret[i][j][0] > 0 and [i, j] != attacker:
                    turrets.append([i, j, self.turret[i][j][0], self.turret[i][j][1]])

        if get_attacker:
            if len(turrets) == 1:
                return None
            attacker = sorted(turrets, key=lambda x: (x[2], -x[3], -(x[0] + x[1]), -x[1]))[0][:2]
            self.turret[attacker[0]][attacker[1]][0] += self.col + self.row
            self.turret[attacker[0]][attacker[1]][1] = round_num
            return attacker
        else:
            return sorted(turrets, key=lambda x: (-x[2], x[3], (x[0] + x[1]), x[1]))[0][:2]

    def _attack_laser(self, attacker: List[int], target: List[int]) -> Optional[List[List[int]]]:
        """
        Step 2 공격 - 레이저 공격
        params:
            attacker
            target
        return:
            turrets: 공격 범위에 있는 포탑
        """
        dx_list = [0, 1, 0, -1]
        dy_list = [1, 0, -1, 0]

        dq = deque()
        dq.append([attacker, [attacker]])
        visited = [[attacker]]

        while dq:
            turret, path = dq.popleft()

            if turret == target:
                break

            for dx, dy in zip(dx_list, dy_list):
                next_x, next_y = (turret[0] + dx) % self.row, (turret[1] + dy) % self.col
                if self.turret[next_x][next_y][0] > 0 and [next_x, next_y] not in visited :
                    dq.append([[next_x, next_y], path+[[next_x, next_y]]])
                    visited.append([next_x, next_y])

        if target not in path:
            return None
        return path

        # def dfs(turret: List[int], visited: List[List[int]]):
        #     """
        #     공격 경로 찾기
        #     """
        #     if turret == target:
        #         return [turret]
        #
        #     path_dict = {}
        #     for pri, (dx, dy) in enumerate(zip(dx_list, dy_list)):
        #         next_x, next_y = (turret[0] + dx) % self.row, (turret[1] + dy) % self.col
        #
        #         if self.turret[next_x][next_y][0] != 0 and [next_x, next_y] not in visited:
        #             path = dfs([next_x, next_y], visited + [turret])
        #             if path:
        #                 path_dict[pri] = [turret] + path
        #
        #     if path_dict:
        #         return sorted(path_dict.items(), key=lambda x: (len(x[1]), x[0]))[0][1]
        #
        # return dfs(attacker, [])

    def _attack_bomb(self, attacker: List[int], target: List[int]):
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
                x, y = (target[0] + dx) % self.row, (target[1] + dy) % self.col
                if self.turret[x][y][0] > 0:
                    turrets.append([x, y])
        return turrets

    def _damage(self, attacker, target, turrets) -> [List[List[int]]]:
        """
        공격 범위에 있는 포탑들 데미지 계산
        param:
            attacker: 공격 포탑
            target: 타겟 포탑
            turrets: 공격 범위에 있는 포탑들
        """
        if turrets:
            for turret in turrets:
                if turret == attacker:
                    continue
                elif turret == target:
                    self.turret[turret[0]][turret[1]][0] -= self.turret[attacker[0]][attacker[1]][0]
                else:
                    self.turret[turret[0]][turret[1]][0] -= self.turret[attacker[0]][attacker[1]][0] // 2

    def _attack(self, attacker: List[int]) -> List[List[int]]:
        """
        Step 2 공격
        레이저 -> 포탄 공격
        params:
            attacker
        return:
            turrets: 공격자, 타겟, 데미지 받은 포탑들
        """
        target = self._get_turret(get_attacker=False, attacker=attacker)
        turrets = self._attack_laser(attacker, target)
        if turrets is None:
            turrets = self._attack_bomb(attacker=attacker, target=target)
        self._damage(attacker, target, turrets)
        return turrets

    def _increase_power(self, turrets: List[List[int]]):
        """
        Step 4 포탑 정비
        :param turrets:
        :return:
        """
        for i in range(self.row):
            for j in range(self.col):
                if self.turret[i][j][0] > 0 and [i, j] not in turrets:
                    self.turret[i][j][0] += 1

    def main(self):
        """
        main function
        """
        step1 = step2 = step3 = 0
        for i in range(1, self.round_num + 1):
            a = time.time()
            attacker = self._get_turret(get_attacker=True, round_num=i)
            b = time.time()
            if attacker is None:
                break
            turrets = self._attack(attacker)
            c = time.time()
            self._increase_power(turrets)
            d = time.time()
            step1 += b-a
            step2 += c-b
            step3 += d-c
        print(f"step1:{step1}, step2:{step2}, step3:{step3}")

        answer = 0
        for i in range(self.row):
            answer = max(answer, max(self.turret[i], key=lambda x: x[0])[0])
        return answer

    def print_turret(self):
        for r in range(self.row):
            print(self.turret[r])


sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/포탑부수기/test1.txt", "r")
T = int(sys.stdin.readline())
for _ in range(T):
    start = time.time()
    solution = Solution()
    print(solution.main())
    print(f"time:{time.time() - start}")
