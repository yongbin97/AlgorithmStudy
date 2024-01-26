def solution(s):
    num_list = sorted(list(map(int, s.split())))
    return f"{num_list[0]} {num_list[-1]}"