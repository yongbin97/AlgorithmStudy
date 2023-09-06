def solution(participant, completion):
    name_dict = {}

    sorted_participant = sorted(participant)
    sorted_completion = sorted(completion)

    for idx in range(len(sorted_participant)):
        if idx == len(sorted_participant) - 1 or sorted_participant[idx] != sorted_completion[idx]:
            return sorted_participant[idx]
