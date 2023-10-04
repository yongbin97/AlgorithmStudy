from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=lambda x: str(x)*10, reverse=True)
        return str(int("".join([str(n) for n in nums])))


solution = Solution()
print(solution.largestNumber([10, 2]))  # 210
print(solution.largestNumber([3, 30, 34, 5, 9]))  # 9534330
print(solution.largestNumber([3, 30, 300, 33, 330]))  # 33333030300
