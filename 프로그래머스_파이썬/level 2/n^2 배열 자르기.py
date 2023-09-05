def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row, col = i // n, i % n
        if row > col:
            answer.append(row+1)
        else:
            answer.append(col+1)
    return answer

# i행 -> i열까지 i, 그 이후 i+1 ...
# x // n : 열, x % n: 행