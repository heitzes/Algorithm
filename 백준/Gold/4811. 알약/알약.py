def dfs(one, half):
    if dp[one][half] != -1:
        return dp[one][half]
    if (one == 0 and half == 0):
        return 1
    cnt = 0
    if one >= 1:
        cnt += dfs(one-1, half+1)
    if half >= 1:
        cnt += dfs(one, half-1) 
    dp[one][half] = cnt
    return dp[one][half]

while True:
    n = int(input())
    if n == 0: break
    dp = [[-1]*2*n for _ in range(n+1)]
    dfs(n, 0)   
    print(dp[n][0])