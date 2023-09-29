from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        answer = 0
        for jewel in jewels:
            answer += counter[jewel]

        return answer