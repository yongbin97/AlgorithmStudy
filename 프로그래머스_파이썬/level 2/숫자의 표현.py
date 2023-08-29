def solution(n):
    answer = 0
    p, q = 1, 0
    while (n - q) / p >= 1:
        if (n - q) % p == 0:
            answer += 1

        q += p
        p += 1

    return answer