import bisect
from typing import List


class Solution:
    def search(self, numbers: List[int], target: int) -> int:
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] < target:
                left = mid + 1
            elif numbers[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers, start=1):
            idx2 = self.search(numbers[idx:], target-num)
            if idx2 != -1:
                return [idx, idx + idx2 + 1]

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers, start=1):
            expect = target - num
            expect_idx = bisect.bisect_left(numbers, expect, lo=idx)

            if expect_idx < len(numbers) and numbers[expect_idx] == expect:
                return [idx, expect_idx+1]



solution = Solution()
print(solution.twoSum2(numbers=[2, 7, 11, 15], target=9))
