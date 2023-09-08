from collections import deque

def solution(maps):
    result = bfs(maps)
    return -1 if result == 0 else result

def bfs(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    dx_list = [1, -1, 0, 0]
    dy_list = [0, 0, 1, -1]
    
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    while q:
        curr_x, curr_y = q.popleft()
        
        for dx, dy in zip(dx_list, dy_list):
            next_dx, next_dy = curr_x + dx, curr_y + dy
            
            if 0 <= next_dx < n and 0 <= next_dy < m:
                if maps[next_dx][next_dy] == 1:
                    if visited[next_dx][next_dy] == 0 or visited[next_dx][next_dy] > visited[curr_x][curr_y] + 1:
                        visited[next_dx][next_dy] = visited[curr_x][curr_y] + 1
                        q.append([next_dx, next_dy])
                    
    return visited[n-1][m-1]
        
            