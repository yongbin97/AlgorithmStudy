from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = list()

        def dfs(n_list: List[int], nums):
            if sum(n_list) == target:
                answer.append(n_list)
                return

            elif sum(n_list) > target:
                return

            for i, n in enumerate(nums):
                dfs(n_list + [n], nums[i:])

        for idx, num in enumerate(candidates):
            dfs([num], candidates[idx:])

        return answer


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))
