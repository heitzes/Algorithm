t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0] * (m+1) for _ in range(n+1)]
    for init in range(1, m//(2**(n-1))+1):
        dp[1][init] = 1
    for i in range(2, n+1):
        for j in range(1, m//(2**(n-i))+1):
            for k in range(1, j//2+1):
                if dp[i-1][k] != 0:
                    dp[i][j] += dp[i-1][k]
    print(sum(dp[n]))