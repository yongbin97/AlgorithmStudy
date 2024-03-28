from collections import deque


def search_robot(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "R":
                return [r, c]

    
def solution(board):
    dr_dc_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    robot = search_robot(board)
    
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    visited[robot[0]][robot[1]] = True
    
    dq = deque()
    dq.append([0, robot[0], robot[1]])
    
    while dq:
        count, curr_r, curr_c = dq.popleft()
        
        for dr, dc in dr_dc_list:
            idx = 0
            while (
                0 <= curr_r + idx * dr < len(board) 
                and 0 <= curr_c + idx * dc < len(board[0])
                and board[curr_r + idx * dr][curr_c + idx * dc] != "D"
            ):
                idx += 1
            next_r = curr_r + (idx - 1) * dr
            next_c = curr_c + (idx - 1) * dc
            
            if board[next_r][next_c] == "G":
                return count + 1
            
            if not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                dq.append([count+ 1, next_r, next_c])
        
    return -1