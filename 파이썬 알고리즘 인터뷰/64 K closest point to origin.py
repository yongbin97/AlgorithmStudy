from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]


solution = Solution()
print(solution.kClosest([[1,3],[-2,2]], 1))
print(solution.kClosest([[3,3],[5,-1],[-2,4]], 2))