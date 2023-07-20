n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + maps[i][j]
answer = -1e9
for k in range(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            r1, c1, r2, c2 = i, j, i+k, j+k
            if r2 <= n and c2 <= n:
                answer = max(answer, dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1])
print(answer)