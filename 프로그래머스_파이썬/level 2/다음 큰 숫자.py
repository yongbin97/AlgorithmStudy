def solution(n):
    answer = n + 1
    count = bin(n)[2:].count("1")
    while bin(answer)[2:].count("1") != count:
        answer += 1

    return answer
