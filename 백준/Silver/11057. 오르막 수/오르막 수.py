n = int(input())
dp = [[0]*10 for _ in range(n+1)]
dp[1] = [1] * 10
for i in range(2, n+1):
    for x in range(10):
        for k in range(x, 10):
            dp[i][x] += dp[i-1][k]
print(sum(dp[n]) % 10007)