from typing import List
from collections import deque, Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dq = deque(maxlen=n)
        heap = []
        answer = len(tasks)

        # set heap
        for task, count in Counter(tasks).items():
            heapq.heappush(heap, (-count, task))

        while heap:
            count, task = heapq.heappop(heap)
            print(f"[start] task:{task}, count:{count}, dq:{dq}, heap:{heap}")

            # if task in dq
            buffer = []
            while task in dq:
                # next task
                if heap:
                    buffer.append((count, task))
                    count, task = heapq.heappop(heap)
                else:
                    dq.append("idle")
                    answer += 1
                    # buffer to heap
                    for task_set in buffer:
                        buffer = []
                        heapq.heappush(heap, task_set)

            # complete task
            if task not in dq:
                dq.append(task)
                if count + 1 != 0:
                    heapq.heappush(heap, (count + 1, task))

            # buffer to heap
            for task_set in buffer:
                heapq.heappush(heap, task_set)

        return answer


solution = Solution()
print(solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))
print(solution.leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
print(solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0))