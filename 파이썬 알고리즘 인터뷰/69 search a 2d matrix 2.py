import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                idx = bisect.bisect_left(matrix[i], target)
                if idx < len(matrix[i]) and matrix[i][idx] == target:
                    return True
            else:
                return False
        return False



solution = Solution()
print(solution.searchMatrix(
    matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
    target=5))
print(solution.searchMatrix(
    matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
    target=20))
print(solution.searchMatrix(
    matrix=[[-5]],
    target=-5))
