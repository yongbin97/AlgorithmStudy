def solution(n):
    fibo_list = [0,1]
    while len(fibo_list) != n + 1:
        fibo_list.append(fibo_list[-2] + fibo_list[-1])
    return fibo_list[-1] % 1234567
