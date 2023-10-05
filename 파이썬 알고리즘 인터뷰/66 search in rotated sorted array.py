from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # step1: find min_value
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # step2: binary search target
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot

        return -1


solution = Solution()
print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
print(solution.search([4, 5, 6, 7, 8, 1, 2, 3], 8))
