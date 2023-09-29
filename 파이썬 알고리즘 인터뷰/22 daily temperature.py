from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i, next_t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < next_t:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)

        return answer


solution = Solution()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(solution.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
