from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        for c in s:
            counter[c] -= 1
            if c in stack:
                continue

            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                stack.pop()

            stack.append(c)
        return ''.join(stack)

solution = Solution()
print(solution.removeDuplicateLetters("bcabc"))