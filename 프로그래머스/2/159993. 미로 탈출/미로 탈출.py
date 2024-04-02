from collections import deque

def move(r, c, start_idx, target, maps):
    dr_dc_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    dq = deque()
    dq.append([r, c])
    
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    visited[r][c] = start_idx
    
    while dq:
        curr_r, curr_c = dq.popleft()
        curr_idx = visited[curr_r][curr_c]
        
        for dr, dc in dr_dc_list:
            next_r, next_c = curr_r + dr, curr_c + dc
            
            if 0 <= next_r < len(maps) and 0 <= next_c < len(maps[0]):
                if maps[next_r][next_c] != "X" and visited[next_r][next_c] == 0:
                    if maps[next_r][next_c] == target:
                        return curr_idx + 1
                    
                    dq.append([next_r, next_c])
                    visited[next_r][next_c] = curr_idx + 1
    return -1

def solution(maps):
    # 출발(S) -> 레버(L) -> 출구(E)
    # 벽만 지나갈 수 없음
    graph = []
    for row in maps:
        graph.append(list(row))
        
    L = [-1, -1]
    S = [-1, -1]
    
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == "L":
                L = [i, j]
            if graph[i][j] == "S":
                S = [i, j]
    L_idx = move(S[0], S[1], 0, "L", graph)
    if L_idx == -1:
        return -1
    else:
        return move(L[0], L[1], L_idx, "E", graph)
