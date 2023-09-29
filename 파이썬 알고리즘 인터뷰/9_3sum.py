from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            left, right = i + 1, len(sorted_nums) - 1
            while left < right:
                sum_3 = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if sum_3 < 0:
                    left += 1
                elif sum_3 > 0:
                    right -= 1
                else:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left += 1
                    while left < right and sorted_nums[right-1] == sorted_nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return result


solution = Solution()

nums_1 = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums_1))
nums_2 = [0, 1, 1]
print(solution.threeSum(nums_2))
nums_3 = [0, 0, 0]
print(solution.threeSum(nums_3))

