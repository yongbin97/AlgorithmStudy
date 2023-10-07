import heapq

def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)
    
    while works and n > 0:
        work = heapq.heappop(works)
        work += 1
        n -= 1
        if work < 0:
            heapq.heappush(works, work)
    return sum([work ** 2 for work in works])