from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        edge_dict = defaultdict(list)
        for a, b in edges:
            edge_dict[a].append(b)
            edge_dict[b].append(a)

        leaves = [a for a in edge_dict.keys() if len(edge_dict[a]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = edge_dict[leaf].pop()
                edge_dict[neighbor].remove(leaf)

                if len(edge_dict[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves

solution = Solution()
print(solution.findMinHeightTrees(5, [[0,1],[0,2],[0,3],[3,4]]))