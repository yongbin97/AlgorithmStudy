def solution(n, a, b):
    count = 0
    total_round = len(bin(n)) - 3

    left, right = 0, n

    while left < right:
        mid = (left + right) / 2
        if mid >= a and mid >= b:
            right = mid
        elif mid < a and mid < b:
            left = mid
        else:
            break
        count += 1

    return total_round - count