class Solution:
    @staticmethod
    def expand(left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""
        for i in range(len(s)):
            result = max(result, self.expand(i, i, s), self.expand(i, i+1, s), key=len)
        return result


solution = Solution()
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("abbad"))
