import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
idx_list = deque(map(int, sys.stdin.readline().split()))
rotate_qu = deque(range(1, N+1))
count = 0
while len(idx_list) != 0:
    if rotate_qu[0] == idx_list[0]:
        rotate_qu.popleft()
        idx_list.popleft()
        M -= 1

    else:
        target_idx = rotate_qu.index(idx_list[0])
        length = len(rotate_qu) 
        if length//2 < target_idx:
            rotate_qu.rotate(length-target_idx)
            count += length-target_idx
        else:
            rotate_qu.rotate(-1 * target_idx)
            count += target_idx

print(count)