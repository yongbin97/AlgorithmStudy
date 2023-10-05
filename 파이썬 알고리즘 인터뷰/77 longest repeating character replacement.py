from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counter = Counter()

        for right, char in enumerate(s, 1):
            counter[char] += 1
            max_char_n = counter.most_common(1)[0][1]

            if right - left - max_char_n > k:
                counter[s[left]] -= 1
                left += 1

        return right - left


solution = Solution()
print(solution.characterReplacement(s="ABAB", k=2))
print(solution.characterReplacement(s="AABABBA", k=1))
