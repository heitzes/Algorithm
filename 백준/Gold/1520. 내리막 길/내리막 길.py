import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*(m) for _ in range(n)]
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
def dfs(x, y):
    global n, m
    if dp[x][y] != -1:
        return dp[x][y]
    if (x, y) == (n-1, m-1):
        return 1
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0<=nx<n and 0<=ny<m): continue
        if maps[nx][ny] < maps[x][y]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]
dfs(0, 0)
print(dp[0][0])