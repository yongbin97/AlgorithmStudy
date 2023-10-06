import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = max_sum = nums[0]
        for num in nums[1:]:
            if curr + num > num:
                curr += num
            else:
                curr = num
            max_sum = max(max_sum, curr)

        return max_sum

    def maxSubArray(self, nums:List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(current_sum, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum


solution = Solution()
print(solution.maxSubArray(nums=[-2, 1]))
print(solution.maxSubArray(nums=[-2, -3]))
print(solution.maxSubArray(nums=[-4, -3]))
print(solution.maxSubArray(nums=[-1, 0, -2]))
print(solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
