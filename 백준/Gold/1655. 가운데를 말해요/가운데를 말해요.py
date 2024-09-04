"""
지금까지 말한 수 중 중간 값
-> list 정렬상태 유지
"""

import sys
import heapq

N = int(sys.stdin.readline())

max_heap = []
min_heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if i % 2 == 0:
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        x, y = -heapq.heappop(max_heap), heapq.heappop(min_heap)
        heapq.heappush(max_heap, -y)
        heapq.heappush(min_heap, x)

    print(-max_heap[0])
