def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball_x, ball_y in balls:
        min_value = m ** 2 + n ** 2
        
        ball_list = [
            [-1 * ball_x, ball_y],
            [ball_x, -1 * ball_y],
            [2 * m - ball_x, ball_y],
            [ball_x, 2 * n - ball_y]
        ]
        
        if ball_x == startX:
            if ball_y < startY:
                ball_list.remove([ball_x, -1 * ball_y])
            else:
                ball_list.remove([ball_x, 2 * n - ball_y])
        
        if ball_y == startY:
            if ball_x < startX:
                ball_list.remove([-1 * ball_x, ball_y])
            else:
                ball_list.remove([2 * m - ball_x, ball_y])
                
        for x, y in ball_list:
            curr = (startX - x) ** 2 + (startY - y) ** 2
            if curr < min_value:
                min_value = curr
        answer.append(min_value)
        
    return answer