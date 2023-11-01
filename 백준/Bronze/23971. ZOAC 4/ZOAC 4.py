import sys

H, W, N, M = map(int, sys.stdin.readline().split())

row = H // (N + 1)
if H % (N + 1) > 0:
    row += 1

col = W // (M + 1)
if W % (M + 1) > 0:
    col += 1

print(row * col)
