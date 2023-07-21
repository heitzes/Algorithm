n = int(input())
nlist = [int(input()) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]
dp[0] = [0, nlist[0], nlist[0]]
for i in range(1, n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + nlist[i]
    dp[i][2] = dp[i-1][1] + nlist[i]
print(max(dp[-1]))