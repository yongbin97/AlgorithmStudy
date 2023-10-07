def solution(m, n, puddles):
    _map = [[0] * m for _ in range(n)]
    
    def dp(a, b):
        # 시작 점
        if a == 0 and b == 0:
            _map[a][b] = 1
            return 1
        # 지도 밖 & 웅덩이
        if (a < 0 or b < 0) or [b+1, a+1] in puddles:
            return 0
        
        if _map[a][b] != 0:
            return _map[a][b]
        _map[a][b] = dp(a, b-1) + dp(a-1, b)
        return _map[a][b]
    
    return dp(n-1, m-1) % 1000000007

