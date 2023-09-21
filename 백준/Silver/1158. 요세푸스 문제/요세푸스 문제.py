import sys

N, K = map(int, sys.stdin.readline().split())

n_list = [i for i in range(1, N+1)]
answer = []
cur = 0
while n_list:
    cur = (cur - 1 + K) % len(n_list)
    answer.append(str(n_list[cur]))
    del n_list[cur]

print(f"<{', '.join(answer)}>")