import math


def solution(r1, r2):
    answer = 0
    
    int_sqrt_r1 = math.ceil(r1 * (1/math.sqrt(2)))
    int_sqrt_r2 = math.floor(r2 * (1/math.sqrt(2)))
    
    for y in range(0, int_sqrt_r2 + 1):
        if y > r1:
            min_x = y
        else:
            min_x = max(math.ceil(math.sqrt(r1 ** 2 - y ** 2)), y)
        max_x = math.floor(math.sqrt(r2 ** 2 - y ** 2))
        x_count = max_x - min_x + 1
        if y == 0:
            answer += x_count
        else:
            answer += 2 * x_count
    
    answer -= int_sqrt_r2 - int_sqrt_r1 + 1
    
    return answer * 4