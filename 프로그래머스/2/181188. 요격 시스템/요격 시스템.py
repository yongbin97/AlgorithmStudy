def solution(targets):
    answer = 0
    
    e = 0
    
    for target in sorted(targets, key=lambda x: [x[1], x[0]]):
        if target[0] >= e:
            answer += 1
            e = target[1]
    
    return answer