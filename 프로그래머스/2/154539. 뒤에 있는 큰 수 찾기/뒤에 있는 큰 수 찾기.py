def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []
    
    for i, num in enumerate(numbers):
        while stack and stack[-1][1] < num:
            idx, _ = stack.pop()
            answer[idx] = num         
                
        stack.append([i, num])
    return answer