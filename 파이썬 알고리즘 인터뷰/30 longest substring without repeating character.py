class MySolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, max_len = 0, 0, 0
        substring = ""

        while end < len(s):
            print(f"start={start}, end={end}, substring={substring}")
            if s[end] not in substring:
                substring += s[end]
                max_len = max(max_len, len(substring))
                end += 1

            else:
                substring = ""
                while end < len(s):
                    start += 1
                    end = start+max_len
                    substring = s[start:end]

                    if len(set(substring)) != max_len:
                        continue
                    else:
                        break

        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length, start = 0, 0

        for idx, char in enumerate(s):
            print(f"idx={idx}, used={used}, start={start}, char={char}")
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, idx - start + 1)

            used[char] = idx

        return max_length

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
