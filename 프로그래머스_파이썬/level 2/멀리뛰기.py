count_dict = {1: 1, 2: 2}

def solution(n):
    answer = 0
    for i in range(3, n + 1):
        count_dict[i] = count_dict[i-1] + count_dict[i-2]
    return count_dict[n] % 1234567
