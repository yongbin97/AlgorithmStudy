def solution(sequence, k):
    print(len(sequence))
    answer = []
    start = end = 0
    curr_sum = sequence[start]
    
    while start < len(sequence) and end < len(sequence):
        # print(f"start: {start}, end: {end}, sum: {curr_sum}, answer: {answer}")
        if curr_sum < k:
            end += 1
            if end < len(sequence):
                curr_sum += sequence[end]

        elif curr_sum > k:
            if start == end:
                break
            
            curr_sum -= sequence[start]
            start += 1
            
        else:
            if len(answer) == 0 or end - start < answer[1] - answer[0]:
                answer = [start, end]
            end += 1
            
            if end < len(sequence):
                curr_sum += sequence[end]
            
    return answer