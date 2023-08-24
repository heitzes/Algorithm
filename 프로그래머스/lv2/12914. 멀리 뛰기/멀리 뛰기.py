def solution(n):
    answer = 0
    dp = [1, 2, 3]
    for i in range(3, n):
        dp.append((dp[i-2] + dp[i-1]) % 1234567)
    return dp[n-1]