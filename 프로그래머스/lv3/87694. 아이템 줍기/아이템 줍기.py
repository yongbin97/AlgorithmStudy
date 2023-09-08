from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    maps = set_maps(rectangle)
    count = bfs(maps, 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY)
    
    return count/2

def set_maps(rectangle):
    maps = [[-1] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = [2 * i for i in r]
        
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    maps[x][y] = 0
                elif maps[x][y] != 0:
                    maps[x][y] = 1
                    
    return maps

def bfs(maps, start_x, start_y, end_x, end_y):
    q = deque()
    q.append([start_x, start_y])
    visited = [[0] * 102 for _ in range(102)]

    dx_list = [1, -1, 0, 0]
    dy_list = [0, 0, 1, -1]
    
    while q:
        curr_x, curr_y = q.popleft()
        
        for dx, dy in zip(dx_list, dy_list):
            next_x, next_y = curr_x + dx, curr_y + dy
            
            if maps[next_x][next_y] == 1:
                if visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = visited[curr_x][curr_y] + 1
                    q.append([next_x, next_y])
                else:
                    visited[next_x][next_y] = min(visited[next_x][next_y], visited[curr_x][curr_y] + 1)
    
    return visited[end_x][end_y]
    
    
    
    