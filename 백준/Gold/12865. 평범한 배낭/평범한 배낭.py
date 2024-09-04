"""
물건 N개
무게 W, 가치 V
K만큼 담을 수 있는 배낭
"""
import sys

N, K = map(int, sys.stdin.readline().split())

dp = [0] * (K + 1)
wv_list = []

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    wv_list.append([W, V])

wv_list.sort(key=lambda x: (-x[1], x[0]))

for w, v in wv_list:
    for idx in range(K, w - 1, -1):
        dp[idx] = max(dp[idx], dp[idx - w] + v)

print(max(dp))

