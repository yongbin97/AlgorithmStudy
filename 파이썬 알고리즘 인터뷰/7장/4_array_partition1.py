from typing import List
from itertools import combinations


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        for i in sorted(nums)[::2]:
            result += i
        return result


solution = Solution()
nums = [1, 4, 3, 2]
print(solution.arrayPairSum(nums))
nums_2 = [6,2,6,5,1,2]
print(solution.arrayPairSum(nums_2))