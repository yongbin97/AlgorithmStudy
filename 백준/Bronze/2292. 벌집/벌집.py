import sys

n = int(sys.stdin.readline())

x = 1
idx = 1
while x < n:
    x += idx * 6
    idx += 1

print(idx)
