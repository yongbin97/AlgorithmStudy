import heapq


def solution(scoville, K):
    start = len(scoville)

    min_value = heapq.heappop(scoville)
    while len(scoville) > 0 and min_value < K:
        min2_value = heapq.heappop(scoville)
        heapq.heappush(scoville, min_value + 2 * min2_value)

        min_value = heapq.heappop(scoville)

    if min_value < K:
        return -1

    return start - len(scoville) - 1


import heapq


def solution1(scoville, K):
    start = len(scoville)
    hq = []
    for s in scoville:
        heapq.heappush(hq, s)

    min_value = heapq.heappop(hq)
    while len(hq) > 0 and min_value < K:
        min2_value = heapq.heappop(hq)
        heapq.heappush(hq, min_value + 2 * min2_value)

        min_value = heapq.heappop(hq)

    if min_value < K:
        return -1

    return start - len(hq) - 1


import heapq


def solution3(scoville, K):
    heapq.heapify(scoville)

    count = 0
    while scoville[0] < K:
        try:
            heapq.heappush(
                scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2
            )
        except IndexError:
            return -1
        count += 1

    return count