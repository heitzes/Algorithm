n = int(input())
nlist = list(map(int, input().split()))
dp = [[0] * (21) for _ in range(n-1)]
dp[0][nlist[0]] = 1 
for i in range(1, n-1):
    for j in range(21):
        if (0 <= j-nlist[i] <= 20) and dp[i-1][j-nlist[i]] != 0:
            dp[i][j] += dp[i-1][j-nlist[i]]
        if (0 <= j+nlist[i] <= 20) and dp[i-1][j+nlist[i]] != 0:
            dp[i][j] += dp[i-1][j+nlist[i]]
print(dp[n-2][nlist[-1]])