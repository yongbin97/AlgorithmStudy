def solution(k, tangerine):
    answer = 0
    size_dict = {}
    for i in tangerine:
        if size_dict.get(i) is None:
            size_dict[i] = 1
        else:
            size_dict[i] += 1

    size_tuple_list = sorted(size_dict.items(), key=lambda x: x[1], reverse=True)

    for size, count in size_tuple_list:
        if k <= 0:
            return answer
        k -= count
        answer += 1

    return answer