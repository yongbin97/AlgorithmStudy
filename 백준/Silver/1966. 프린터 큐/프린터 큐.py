import sys
from collections import deque

testcase_num = int(sys.stdin.readline())

for _ in range(testcase_num):
    n, m = map(int, sys.stdin.readline().split())
    prior_list = deque(map(int, sys.stdin.readline().split()))

    idx_list = deque(range(1, n+1))
    target = idx_list[m]
    count = 1
    maxPrior = max(prior_list)

    while len(idx_list) != 0:

        idx = idx_list.popleft()
        prior = prior_list.popleft()

        if prior == maxPrior:
            if idx == target:
                print(count)
                break
            else:
                maxPrior = max(prior_list)
                count += 1

        else:
            idx_list.append(idx)
            prior_list.append(prior)



