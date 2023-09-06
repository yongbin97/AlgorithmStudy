import math


def solution(progresses, speeds):
    answer = []

    curr_day = 0
    count = 0
    for idx, progress in enumerate(progresses):
        remain = math.ceil((100 - progress) / speeds[idx])
        if curr_day >= remain:
            count += 1
        else:
            if count != 0:
                answer.append(count)
            curr_day = remain
            count = 1

    if count > 0:
        answer.append(count)
    return answer