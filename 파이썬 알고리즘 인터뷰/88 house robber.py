from collections import defaultdict
from typing import List


class Solution:
    money = defaultdict(int)

    def rob(self, nums: List[int]) -> int:
        def get_money(idx):
            if idx < 0:
                return 0
            elif idx < 2:
                return nums[idx]

            if self.money[idx]:
                return self.money[idx]
            self.money[idx] = get_money(idx - 2) + get_money(idx - 3) + nums[n]
            return self.money[idx]

        for n in range(len(nums)):
            self.money[n] = max(get_money(n - 2), get_money(n - 3)) + nums[n]

        return max(self.money.values())

    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = {}
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp.popitem()[1]


solution = Solution()
print(solution.rob(nums=[0]))  # 4
print(solution.rob(nums=[1, 2, 3, 1]))  # 4
print(solution.rob(nums=[2, 7, 9, 3, 1]))  # 12
print(solution.rob(nums=[7, 2, 3, 9]))  # 16
print(solution.rob(nums=[7, 8, 3, 9]))  # 17
