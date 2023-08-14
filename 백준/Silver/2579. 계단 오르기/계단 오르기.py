n = int(input())
nlist = [int(input()) for _ in range(n)]
if n == 1:
    print(nlist[0])
else:
    dp = [[[0, 0] for _ in range(2)] for _ in range(n)]
    dp[0][0] = [nlist[0], nlist[0]]
    dp[1][0] = [nlist[0]+nlist[1], nlist[1]]
    dp[1][1] = [nlist[0], 0]
    for i in range(2, n):
        dp[i][0][0] = dp[i-1][0][1] + nlist[i]
        dp[i][0][1] = dp[i-1][1][0] + nlist[i]
        dp[i][1][0] = max(dp[i-1][0])
        dp[i][1][1] = max(dp[i-2][0])
    print(max(dp[-1][0]))