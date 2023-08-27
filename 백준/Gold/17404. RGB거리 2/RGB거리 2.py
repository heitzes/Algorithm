n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9
for i in range(3):
    dp = [[1e9, 1e9, 1e9] for _ in range(n)]
    dp[0][i] = nlist[0][i]
    for k in range(1, n):
        dp[k][0] = min(dp[k-1][1], dp[k-1][2]) + nlist[k][0]
        dp[k][1] = min(dp[k-1][0], dp[k-1][2]) + nlist[k][1]
        dp[k][2] = min(dp[k-1][0], dp[k-1][1]) + nlist[k][2]
    for k in range(3):
        if i != k:
            answer = min(dp[-1][k], answer)
print(answer)