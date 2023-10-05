from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = dict(Counter(t))
        need_count = len(t)
        left = 0
        start = end = -1

        for right, char in enumerate(s, start=1):
            # right
            if char in target.keys():
                if target[char] > 0:
                    need_count -= 1
                target[char] -= 1

            # left
            while left < right and target.get(s[left], -1) < 0:
                if s[left] in target.keys():
                    target[s[left]] += 1

                left += 1
            # set new start, end
            if need_count <= 0 and (start == end == -1 or right-left < end-start):
                start, end = left, right
        return s[start: end]


solution = Solution()
print(solution.minWindow(s="ADOBECODEBANC", t="ABC"))
print(solution.minWindow(s="acbbaca", t="aba"))
print(solution.minWindow(s="aaaaaaaaaaaabbbbbcdd", t="abcdd"))

