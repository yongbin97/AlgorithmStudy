def solution(n):
    answer = ""
    while n:
        if n % 3 == 0:
            answer += "4"
            n = n //3 -1
            
        else:
            answer += str(n%3)
            n = n // 3 
            
    return answer[::-1]

# n = 3*a + b
# 1, 2, 3(4)
# 3 = 3 * 1 + 0
# 4 = 3 * 1 + 1
# 5 = 3 * 1 + 2
# 6 = 3 * 2 + 0
# 7 = 3 * 2 + 1