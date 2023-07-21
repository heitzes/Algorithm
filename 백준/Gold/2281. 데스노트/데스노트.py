n, m = map(int, input().split())
nlist = [int(input()) for _ in range(n)]
dp = [[-1]* (m+1) for _ in range(n)]
def dfs(ind, remain):
    global n, m
    if ind == n: return 0
    if dp[ind][remain] != -1: return dp[ind][remain]
    dp[ind][remain] = (min(remain+1, m))**2 + dfs(ind+1, m-(nlist[ind]+1))
    if remain - nlist[ind] >= 0: ## 같은 줄 가능
        dp[ind][remain] = min(dp[ind][remain], dfs(ind+1, remain-(nlist[ind]+1)))
    return dp[ind][remain]
dfs(0, m)
print(dp[0][m])