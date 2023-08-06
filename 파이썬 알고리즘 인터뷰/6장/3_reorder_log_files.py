from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit, letter = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letter + digit

log_test_case_1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
log_test_case_2 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
log_test_case_3 = ["1 n u", "r 527", "j 893", "6 14", "6 82"]

solution = Solution()
print(solution.reorderLogFiles(log_test_case_1))
print(solution.reorderLogFiles(log_test_case_2))
print(solution.reorderLogFiles(log_test_case_3))
