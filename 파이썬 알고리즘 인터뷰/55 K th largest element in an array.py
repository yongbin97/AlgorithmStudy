from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, (-n, n))
        for _ in range(k):
            _, x = heapq.heappop(heap)
        return x