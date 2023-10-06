from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        answer = 0
        for child in sorted(g):
            # 현재 아이의 greed 값보다 작은 쿠키 버리기
            while s and child > s[-1]:
                s.pop()
            if s and child <= s.pop():
                answer += 1
        return answer


solution = Solution()
print(solution.findContentChildren(g=[1, 2, 3], s=[1, 1]))
print(solution.findContentChildren(g=[10, 9, 8, 7], s=[5, 6, 7, 8]))
