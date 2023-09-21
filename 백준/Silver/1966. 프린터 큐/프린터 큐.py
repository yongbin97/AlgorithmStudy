import sys
from collections import deque


test_count = int(sys.stdin.readline())

for _ in range(test_count):
    N, M = map(int, sys.stdin.readline().split())
    x = sys.stdin.readline().split()
    tuple_list = deque((int(p), i) for i, p in enumerate(x))

    answer = 1
    while tuple_list:
        curr_p, curr_i = tuple_list.popleft()
        if any(curr_p  < p for p, _ in tuple_list):
            tuple_list.append((curr_p, curr_i))

        else:
            if curr_i == M:
                print(answer)
            else:
                answer += 1



