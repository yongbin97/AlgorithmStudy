from typing import List
from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in result:
                        result.append([nums[i], nums[j], nums[k]])

        return result


solution = Solution()

nums_1 = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums_1))
nums_2 = [0, 1, 1]
print(solution.threeSum(nums_2))
nums_3 = [0, 0, 0]
print(solution.threeSum(nums_3))

