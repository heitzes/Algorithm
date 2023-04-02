def solution(triangle):
    """
    점화식: DP[n][k] = MAX(DP[n-1][k-1], DP[n-1][k]) + triangle[n][k] (단, k는 양 끝이 아님)
    """
    height = len(triangle)
    dp = [[0 for _ in range(i)] for i in range(1, height+1)]
    dp[0][0] = triangle[0][0]
    for n in range(1, height):
        for k in range(n+1):
            if k != 0 and k != n:
                dp[n][k] = max(dp[n-1][k-1], dp[n-1][k]) + triangle[n][k]
            elif k == 0:
                dp[n][0] = dp[n-1][0] + triangle[n][0]
            elif k == n:
                dp[n][k] = dp[n-1][k-1] + triangle[n][k]
    return max(dp[-1])