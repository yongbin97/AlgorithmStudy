def solution(clothes):
    answer = 1
    closet = {}
    for cloth, cloth_type in clothes:
        if closet.get(cloth_type) is None:
            closet[cloth_type] = [cloth]
        else:
            closet[cloth_type].append(cloth)

    for cloth_type, cloth_list in closet.items():
        answer *= len(cloth_list) + 1

    return answer - 1