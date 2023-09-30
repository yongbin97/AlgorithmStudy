from typing import List


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


solution = Solution()
print(solution.permute([1, 2, 3]))
