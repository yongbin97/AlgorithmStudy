import sys


class CustomSet:
    def __init__(self):
        self._set = set()

    def add(self, x):
        self._set.add(x)

    def remove(self, x):
        if self.check(x):
            self._set.remove(x)

    def check(self, x):
        if x in self._set:
            return 1
        else:
            return 0

    def toggle(self, x):
        if self.check(x):
            self.remove(x)
        else:
            self.add(x)

    def all(self):
        self._set = set(i for i in range(1, 21))

    def empty(self):
        self._set = set()


M = int(sys.stdin.readline())
S = CustomSet()

for _ in range(M):
    operation = sys.stdin.readline().split()

    if operation[0] == "add":
        S.add(int(operation[1]))

    elif operation[0] == "remove":
        S.remove(int(operation[1]))

    elif operation[0] == "check":
        print(S.check(int(operation[1])))

    elif operation[0] == "toggle":
        S.toggle(int(operation[1]))

    elif operation[0] == "all":
        S.all()

    else:
        S.empty()
