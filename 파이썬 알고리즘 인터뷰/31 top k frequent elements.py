from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for n in nums:
            if freq_dict.get(n) is None:
                freq_dict[n] = 1
            else:
                freq_dict[n] += 1
        sorted_dict = sorted(freq_dict.items(), key=lambda v: v[1], reverse=True)
        return [pair[0] for pair in sorted_dict[:k]]

    def topKFrequent_2(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [pair[0] for pair in counter.most_common(k)]


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(solution.topKFrequent_2([1, 1, 1, 2, 2, 3], 2))
