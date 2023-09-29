from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx, num in enumerate(nums):
            if num_dict.get(num) is not None and num * 2 == target:
                return [num_dict[num], idx]
            num_dict[num] = idx

        for idx, num in enumerate(nums):
            target_num = target - num
            if target_num != num and num_dict.get(target_num) is not None:
                return [idx, num_dict.get(target_num)]


solution = Solution()

nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum2(nums, target))

nums = [3, 2, 4]
target = 6
print(solution.twoSum2(nums, target))

nums = [3, 3]
target = 6
print(solution.twoSum2(nums, target))
nums = [2,5,5,11]
target = 10
print(solution.twoSum2(nums, target))
