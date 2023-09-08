import sys

N = int(sys.stdin.readline())
num = int(sys.stdin.readline())

network = {i+1: [] for i in range(N)}
for _ in range(num):
    a, b = list(map(int, sys.stdin.readline().split()))
    network[a].append(b)
    network[b].append(a)

computers = [i+1 for i in range(N)]

def dfs(com):
    # end
    if com not in computers:
        return

    # visited
    if com in computers:
        computers.remove(com)

    # next
    connected = network[com]
    for com in connected:
        dfs(com)

dfs(1)
print(N - len(computers) -1)
