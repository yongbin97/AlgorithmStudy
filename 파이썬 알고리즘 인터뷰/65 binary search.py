import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid, left, right = 0, 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] != target and left == mid:
                return -1
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                return mid

        return mid

    def search2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1


solution = Solution()
print(solution.search2([-1,0,3,5,9,12],12))
print(solution.search2([-1,0,3,5,9,12],2))