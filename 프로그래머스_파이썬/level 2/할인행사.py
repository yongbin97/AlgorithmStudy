def solution(want, number, discount):
    answer = 0

    for i in range(len(discount) - 9):
        item_dict = dict(zip(want, number))
        for j in range(i, i + 10):
            if item_dict.get(discount[j], 0) != 0:
                item_dict[discount[j]] -= 1
        if sum(item_dict.values()) == 0:
            answer += 1

    return answer

