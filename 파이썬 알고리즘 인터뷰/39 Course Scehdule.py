from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        traced = set()
        visited = set()

        pre_dict = defaultdict(list)
        for a, b in prerequisites:
            pre_dict[a].append(b)

        def dfs(x):
            if x in traced:
                return False
            if x in visited:
                return True

            traced.add(x)
            for y in pre_dict[x]:
                if not dfs(y):
                    return False
            traced.remove(x)
            visited.add(x)

            return True

        for x in range(numCourses):
            if not dfs(x):
                return False

        return True


solution = Solution()
print(solution.canFinish(3, [[0,1], [1,2], [0, 2]]))

