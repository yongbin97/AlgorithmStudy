from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]]
        for left, right in intervals[1:]:
            prev_left, prev_right = answer.pop()
            if left <= prev_right:
                answer.append([prev_left, max(right, prev_right)])
            else:
                answer.append([prev_left, prev_right])
                answer.append([left, right])

        return answer



solution = Solution()
print(solution.merge([[2, 6], [1, 3], [8, 10], [15, 18]]))
print(solution.merge([[1,4],[0,4]]))
