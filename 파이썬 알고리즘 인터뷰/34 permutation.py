from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(n_list):
            if len(n_list) == len(nums):
                return answer.append(n_list)

            for n in nums:
                if n not in n_list:
                    dfs(n_list + [n])

        for num in nums:
            dfs([num])

        return answer

    def permute_2(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, permutations(nums)))


solution = Solution()
print(solution.permute([1, 2, 3]))
print(solution.permute_2([1, 2, 3]))
