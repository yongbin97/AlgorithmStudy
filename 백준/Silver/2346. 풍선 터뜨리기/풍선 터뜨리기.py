import sys


N = int(sys.stdin.readline())
b_list = [(i, m) for i, m in enumerate(list(map(int, sys.stdin.readline().split())), start=1)]
curr = 0


answer = []
while b_list:
    curr_b = b_list[curr]
    b_list.remove(curr_b)
    # answer.append(curr_b[0])
    print(curr_b[0], end=' ')
    curr += curr_b[1]
    if b_list:
        if curr_b[1] > 0:
            curr = (curr - 1) % len(b_list)
        else:
            curr %= len(b_list)
