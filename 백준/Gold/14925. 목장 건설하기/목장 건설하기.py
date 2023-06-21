import sys
sys.setrecursionlimit(10**6)
m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    if x == m-1 or y == n-1:
        if maps[x][y] == 0:
            dp[x][y] = 1
            return 1
        dp[x][y] = 0
        return 0
    if maps[x][y] == 0:
        dp[x][y] = min(dfs(x+1, y), dfs(x, y+1), dfs(x+1, y+1)) + 1 
    else:
        dp[x][y] = 0
    return dp[x][y]
answer = 0
for i in range(m):
    for j in range(n):
        answer = max(answer, dfs(i, j))
print(answer)