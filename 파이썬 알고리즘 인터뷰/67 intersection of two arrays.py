from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1, set_2 = set(nums1), set(nums2)
        return list(set_1.intersection(set_2))


solution = Solution()
print(solution.intersection([1, 2, 2, 1], [2, 2]))
print(solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
print(solution.intersection([], [9, 4, 9, 8, 4]))
