import sys

N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().strip().split()))

answer = [str(0)] * N

stack = []
for i, t in enumerate(tower[::-1]):
    while stack and stack[-1][0] <= t:
        _, idx = stack.pop()
        answer[idx-1] = str(N-i)

    stack.append((t, N-i))

print(" ".join(answer))