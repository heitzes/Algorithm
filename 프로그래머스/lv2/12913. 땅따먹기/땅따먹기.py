def solution(land):
    dp = [[0,0,0,0] for _ in range(len(land))]
    dp[0] = land[0]
    for i in range(1, len(land)):
        for j in range(4):
            dp[i][j] = max([dp[i-1][k] if k!=j else 0 for k in range(4)]) + land[i][j]    
    return max(dp[-1])