from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for s_char in s:
            s_dict[s_char] += 1
        for t_char in t:
            t_dict[t_char] += 1
        return s_dict == t_dict

    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))