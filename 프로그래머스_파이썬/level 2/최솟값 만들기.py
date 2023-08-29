def solution(A, B):
    answer = 0

    a_list = sorted(A)
    b_list = sorted(B)
    b_list.reverse()

    for i in range(len(a_list)):
        answer += a_list[i] * b_list[i]

    return answer


def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
