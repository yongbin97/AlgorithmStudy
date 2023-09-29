from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
        prefix, suffix = [1], [1]

        for i in range(length - 1):
            prefix.append(prefix[i] * nums[i])
            suffix.append(suffix[i] * nums[length-i-1])

        for i in range(length):
            result.append(prefix[i] * suffix[length-i-1])

        return result


solution = Solution()
nums_1 = [1, 2, 3, 4]
print(solution.productExceptSelf(nums_1))
nums_2 = [-1, 1, 0, -3, 3]
print(solution.productExceptSelf(nums_2))
