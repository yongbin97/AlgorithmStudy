def solution(answers):
    count = [0, 0, 0]
    answer_1 = [1, 2, 3, 4, 5]
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx, answer in enumerate(answers):
        if answer_1[idx % len(answer_1)] == answer:
            count[0] += 1
        if answer_2[idx % len(answer_2)] == answer:
            count[1] += 1
        if answer_3[idx % len(answer_3)] == answer:
            count[2] += 1

    answ = []
    for i, c in enumerate(count, start=1):
        if c == max(count):
            answ.append(i)

    return answ

# 1번: 1,2,3,4,5             5
# 2번: 2,1,2,3,2,4,2,5       8
# 3번: 3,3,1,1,2,2,4,4,5,5   10