from typing import List
from collections import deque, defaultdict
import heapq


class Solution:
    # use dijkstra
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = defaultdict(list)
        for start, end, time in times:
            network[start].append((end, time))

        dist = defaultdict(int)

        # (time, node)
        heap = [(0, k)]

        while heap:
            curr_time, curr_node = heapq.heappop(heap)
            dist[curr_node] = curr_time
            for next_node, next_time in network[curr_node]:
                if dist.get(next_node) is None:
                    heapq.heappush(heap, (curr_time + next_time, next_node))

        if len(dist) == n:
            return max(dist.values())
        else:
            return -1



    def networkDelayTime_2(self, times: List[List[int]], n: int, k: int) -> int:
        # visited[a] => time of n node receive signal
        visited_time = [-1] * n
        network = defaultdict(list)
        for start, end, time in times:
            network[start - 1].append((end - 1, time))
        dq = deque()

        visited_time[k - 1] = 0
        dq.append(k - 1)
        while dq:
            curr_node = dq.popleft()
            for end, time in network[curr_node]:
                # not visited or update min visited value
                if visited_time[end] == -1 or visited_time[curr_node] + time < visited_time[end]:
                    visited_time[end] = visited_time[curr_node] + time
                    dq.append(end)

        if -1 in visited_time:
            return -1
        else:
            return max(visited_time)


solution = Solution()
print(solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(solution.networkDelayTime([[1, 2, 1]], 2, 1))
print(solution.networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1))
