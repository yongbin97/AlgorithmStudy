from collections import deque


def solution(people, limit):
    answer = 0
    dq = deque(sorted(people))

    while len(dq) > 0:
        weight = limit - dq.pop()

        if len(dq) > 0 and weight >= dq[0]:
            dq.popleft()
        answer += 1

    return answer

# sorted by weight desc
# [10, 20, 30, 60, 80, 100] 100
# 문제 잘 읽자 용빈아 눈은 어디에 두고 다니는 거니 이 멍청ㅎㄴ...
