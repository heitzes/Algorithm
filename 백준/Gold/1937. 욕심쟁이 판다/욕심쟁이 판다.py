import sys
sys.setrecursionlimit(10**6)
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
def dfs(x, y):
    if dp[x][y] != -1: return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0<=nx<n and 0<=ny<n): continue
        if board[nx][ny] > board[x][y]:
            dp[x][y] = max(dfs(nx, ny), dp[x][y])
    dp[x][y] += 1
    return dp[x][y]
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            dfs(i, j)
print(max([max(row) for row in dp]))