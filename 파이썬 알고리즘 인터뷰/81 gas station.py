from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return - 1

        start, fuel = 0, 0
        for idx in range(len(gas)):
            if fuel + gas[idx] < cost[idx]:
                start = idx + 1
                fuel = 0
            else:
                fuel += gas[idx] - cost[idx]

        return start



solution = Solution()
print(solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))  # 3
print(solution.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))  # -1
print(solution.canCompleteCircuit(gas=[5, 8, 2, 8], cost=[6, 5, 6, 6]))  # 3
