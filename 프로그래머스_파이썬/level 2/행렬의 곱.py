def solution(arr1, arr2):
    answer = []
    for ar1 in arr1:
        row_list = []
        for col in range(len(arr2[0])):
            new_element = 0
            for idx, a1 in enumerate(ar1):
                new_element += a1 * arr2[idx][col]
            row_list.append(new_element)
        answer.append(row_list)

    return answer
