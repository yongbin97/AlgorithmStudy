from typing import List
import heapq

class Solution:
    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        answer = []
        while people:
            p = people.pop()
            answer.insert(p[1], p)
        return answer

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for p in people:
            heapq.heappush(heap, (-p[0], p[1]))

        result = []
        while heap:
            h, k = heapq.heappop(heap)
            result.insert(k, [-h, k])
        return result








solution = Solution()
print(solution.reconstructQueue(people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
