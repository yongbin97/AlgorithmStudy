from collections import deque


def bfs(x, y, n):
    if x == y:
        return 0
    
    count = [0 for _ in range(y)]
    
    dq = deque()
    dq.append(x)
    
    while dq:
        curr_x = dq.popleft()
        
        # 정답
        if curr_x + n == y or 2 * curr_x == y or 3 * curr_x == y:
            return count[curr_x] + 1
        
        # NEXT
        if curr_x + n < y and count[curr_x + n] == 0:
            dq.append(curr_x + n)
            count[curr_x + n] = count[curr_x] + 1
        if 2 * curr_x < y and count[2 * curr_x] == 0:
            dq.append(2 * curr_x)
            count[2 * curr_x] = count[curr_x] + 1
        if 3 * curr_x < y and count[3 * curr_x] == 0:
            dq.append(3 * curr_x)
            count[3 * curr_x] = count[curr_x] + 1
            
    # 만들 수 없는 경우
    return -1
    

def solution(x, y, n):
    return bfs(x,y,n)
