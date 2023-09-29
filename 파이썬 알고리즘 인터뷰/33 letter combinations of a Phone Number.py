from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        answer = []
        def dfs(idx, word):
            if idx >= len(digits):
                answer.append(word)
                return

            char_list = letter_dict[digits[idx]]

            for c in char_list:
                dfs(idx+1, word+c)

        if len(digits):
            dfs(0, "")
        return answer

solution = Solution()
print(solution.letterCombinations(""))
