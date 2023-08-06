import re
from typing import List
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph_alphanumeric = re.sub(r"[^0-9a-zA-Z\s]", " ", paragraph.lower())
        exclude_paragraph = [word for word in paragraph_alphanumeric.split() if word not in banned]
        return Counter(exclude_paragraph).most_common()[0][0]


solution = Solution()

paragraph_1 = "Bob hit a ball, the hit BALL flew far after it was hit."
banned_1 = ["hit"]
print(solution.mostCommonWord(paragraph_1, banned_1))

paragraph_2 = "a."
banned_2 = []
print(solution.mostCommonWord(paragraph_2, banned_2))