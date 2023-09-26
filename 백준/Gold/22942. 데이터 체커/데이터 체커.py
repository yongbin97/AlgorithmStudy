import sys

N = int(sys.stdin.readline())
c_list = list()
for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    c_list.append((x-r, x))
    c_list.append((x+r, x))
c_list.sort()

def check():
    stack = []

    for c in c_list:
        if stack and stack[-1][1] == c[1]:
            stack.pop()

        else:
            stack.append(c)

    if stack:
        return "NO"
    else:
        return "YES"
    
print(check())