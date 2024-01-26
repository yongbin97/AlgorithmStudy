import sys

N, K = map(int, sys.stdin.readline().split())

answ = 0

for i in range(1, N + 1):
    if N % i == 0:
        K -= 1

    if K == 0:
        answ = i
        break

print(answ)
