import sys
from collections import deque


def dfs(curr, result):
    # end
    if visited_dfs[curr-1]:
        return

    # action
    visited_dfs[curr-1] = True
    result.append(curr)

    # next
    for node in lines_dict[curr]:
        dfs(node, result)

    return result

def bfs(start):
    q = deque([start])
    visit_order = []
    while len(q) > 0:
        curr_node = q.popleft()
        visit_order.append(curr_node)
        visited_bfs[curr_node-1] = True

        lines = lines_dict[curr_node]
        for node in lines:
            if not visited_bfs[node-1] and node not in q:
                q.append(node)


    return visit_order


# get data
# N: 정점의 개수, M: 간선의 수, V: 시작점
N, M, V = map(int, sys.stdin.readline().split())

# 간선
lines_dict = {i: [] for i in range(1, N+1)}
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    lines_dict[a].append(b)
    lines_dict[b].append(a)
    lines_dict[a].sort()
    lines_dict[b].sort()


visited_dfs = [False for _ in range(N)]
visited_bfs = [False for _ in range(N)]

print(" ".join(map(str, dfs(V, []))))
print(" ".join(map(str, bfs(V))))


