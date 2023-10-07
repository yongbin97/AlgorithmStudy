def solution(routes):
    cammera = []
    for start, end in sorted(routes):
        flag = False
        for idx, (c_start, c_end) in enumerate(cammera):
            if c_start <= start <= c_end or c_start <= end <= c_end:
                cammera[idx] = [max(c_start, start), min(c_end, end)]
                flag = True
        if not flag:
            cammera.append([start, end])
    return len(cammera)

