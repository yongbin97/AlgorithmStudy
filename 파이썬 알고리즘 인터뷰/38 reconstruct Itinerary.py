from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_dict = defaultdict(list)
        for f, t in sorted(tickets, reverse=True):
            ticket_dict[f].append(t)
        print(ticket_dict)
        result = []

        def dfs(city: str):
            print(f"city={city}, ticket_dict={ticket_dict}")
            while ticket_dict[city]:
                dfs(ticket_dict[city].pop())
            result.append(city)
            print(result)

        dfs("a")

        return result[::-1]

solution = Solution()
print(solution.findItinerary([["a", "b"], ["b", "d"], ["b", "c"], ["c", "b"], ["d", "e"]]))
