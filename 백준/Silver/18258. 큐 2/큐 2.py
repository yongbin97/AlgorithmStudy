import sys
from collections import deque


class MyQueue:
    def __init__(self):
        self._queue = deque()

    def push(self, x: int):
        self._queue.append(x)

    def pop(self) -> int:
        if self._queue:
            return self._queue.popleft()
        else:
            return -1

    def size(self) -> int:
        return len(self._queue)

    def empty(self) -> int:
        return 0 if self._queue else 1

    def front(self) -> int:
        if self._queue:
            return self._queue[0]
        else:
            return -1

    def back(self) -> int:
        if self._queue:
            return self._queue[-1]
        else: return -1


N = int(sys.stdin.readline())
q = MyQueue()
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        q.push(int(command[1]))
    elif command[0] == "pop":
        print(q.pop())
    elif command[0] == "size":
        print(q.size())
    elif command[0] == "empty":
        print(q.empty())
    elif command[0] == "front":
        print(q.front())
    elif command[0] == "back":
        print(q.back())
    else:
        print("wrong command")
