def check(curr_hm, curr_s, last_hm, last_s):
    return (
        curr_s == curr_hm
        or (
            last_s < last_hm 
            and (curr_s >= curr_hm or curr_s == 0 and curr_hm > 354)
        )
    )


def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    last_time_sec, start_time_sec = h2 * 3600 + m2 * 60 + s2, h1 * 3600 + m1 * 60 + s1
    total_time = last_time_sec - start_time_sec
    
    last_degree = [
        start_time_sec / 120 % 360,
        start_time_sec / 10 % 360,
        start_time_sec * 6 % 360
    ]
            
    for t in range(total_time + 1):
        curr_degree = [
            (start_time_sec + t) / 120 % 360,
            (start_time_sec + t) / 10 % 360,
            (start_time_sec + t) * 6 % 360
        ]
        
        # 시침 - 초침
        if check(curr_degree[0], curr_degree[2], last_degree[0] , last_degree[2]):
            answer += 1
        
        # 분침 - 초침
        if check(curr_degree[1], curr_degree[2], last_degree[1] , last_degree[2]):
            answer += 1
        
        # 시침 - 분침 - 초침
#         if curr_degree[0] == curr_degree[1] == curr_degree[2]:
#             answer -= 1
        
        if start_time_sec + t == 0 or start_time_sec + t == 12 * 3600:
            answer -= 1
    
        last_degree = curr_degree
        
    return answer