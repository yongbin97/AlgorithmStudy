from collections import deque
import sys

n = int(sys.stdin.readline())
dq = deque()
for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push_front":
        dq.appendleft(int(command[1]))

    elif command[0] == "push_back":
        dq.append(int(command[1]))

    elif command[0] == "pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())

    elif command[0] == "pop_back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif command[0] == "size":
        print(len(dq))

    elif command[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])

    else:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])