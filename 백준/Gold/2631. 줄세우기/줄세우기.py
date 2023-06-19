n = int(input())
nlist = [int(input()) for _ in range(n)]
dp = [1] * n
for i in range(n):
    for j in range(i):
        if nlist[j] < nlist[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(n - max(dp))