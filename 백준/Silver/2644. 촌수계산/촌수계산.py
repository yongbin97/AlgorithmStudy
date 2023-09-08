import sys

total = int(sys.stdin.readline())
start, target = list(map(int, sys.stdin.readline().split()))
people = [i+1 for i in range(total)]

# parent, child
graph = {i+1: [] for i in range(total)}
for _ in range(int(sys.stdin.readline())):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(curr_p, target, count):
    # end
    if curr_p == target:
        return count

    next_list = [next_p for next_p in graph[curr_p] if next_p in people]
    if len(next_list) == 0:
        return -1

    # action
    people.remove(curr_p)
    count += 1

    # next
    for next_p in next_list:
        res = dfs(next_p, target, count)
        if res != -1:
            return res

    return -1

print(dfs(start, target, 0))
