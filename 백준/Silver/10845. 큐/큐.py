import sys
from collections import deque

N = int(sys.stdin.readline())
qu = deque()

for _ in range(N):
    command = list(sys.stdin.readline().split())

    if command[0] == "pop":
        if len(qu) == 0:
            print(-1)
        else:
            print(qu.popleft())

    elif command[0] == "size":
        print(len(qu))

    elif command[0] == "empty":
        if len(qu) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "front":
        if len(qu) == 0:
            print(-1)
        else:
            print(qu[0])

    elif command[0] == "back":
        if len(qu) == 0:
            print(-1)
        else:
            print(qu[-1])

    else:
        qu.append(command[1])