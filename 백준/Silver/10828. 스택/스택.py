import sys

class stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.empty():
            return -1
        else:
            popItem = self.items.pop()
            return popItem

    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def top(self):
        if self.empty():
            return -1
        else:
            return self.items[-1]


N = int(input())
stk = stack()
for i in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        stk.push(command[1])
    elif command[0] == "pop":
        print(stk.pop())
    elif command[0] == "size":
        print(stk.size())
    elif command[0] == "empty":
        print(int(stk.empty()))
    elif command[0] == "top":
        print(stk.top())