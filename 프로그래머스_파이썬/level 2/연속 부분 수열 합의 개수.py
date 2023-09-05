def solution(elements):
    element_length = len(elements)
    sum_list = []

    for i in range(element_length):
        for j in range(i, i + element_length):
            if j >= element_length:
                sum_list.append(sum(elements[i % element_length:]) + sum(elements[:j % element_length]))

            else:
                sum_list.append(sum(elements[i % element_length: j % element_length]))

    return len(list(set(sum_list)))
