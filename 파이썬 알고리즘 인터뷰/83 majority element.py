from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


solution = Solution()
print(solution.majorityElement(nums=[3, 2, 3]))
print(solution.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
