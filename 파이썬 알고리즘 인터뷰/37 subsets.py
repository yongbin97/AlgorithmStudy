from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(idx, n_list):
            answer.append(n_list)

            for i in range(idx, len(nums)):
                dfs(i+1, n_list + [nums[i]])

        dfs(0, [])

        return answer

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(nums)+1):
            answer += list(map(list, combinations(nums, i)))
        return answer


solution = Solution()
print(solution.subsets([1,2,3]))

