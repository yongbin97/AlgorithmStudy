def solution(triangle):
    for row in range(len(triangle)-2, -1, -1):
        for i  in range(row+1):
            triangle[row][i] += max(triangle[row+1][i], triangle[row+1][i+1])
    
    return triangle[0][0]