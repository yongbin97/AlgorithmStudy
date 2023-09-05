def solution(s):
    answer = []
    set_list = []
    for idx, c in enumerate(s[1:-1], start=1):
        if c == "{":
            left_idx = idx
        elif c == "}":
            set_list.append(s[left_idx + 1: idx].split(","))

    for num_list in sorted(set_list, key=lambda x: len(x)):
        for num in num_list:
            if int(num) not in answer:
                answer.append(int(num))
    return answer