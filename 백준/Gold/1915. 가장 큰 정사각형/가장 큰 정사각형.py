import sys
def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
maps = [list(map(int, list(input()))) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dx, dy = [0, 1, 1], [1, 0, 1]
for i in range(n):
    dp[i][-1] = maps[i][-1]
dp[-1] = maps[-1]
def dfs(x, y):
    global n, m
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = maps[x][y]
    check = 1e9
    for i in range(3):
        check = min(dfs(x+dx[i], y+dy[i]), check)
    dp[x][y] = check+1 if maps[x][y]!=0 else 0
    return dp[x][y]
dfs(0, 0)
print(max([max(row) for row in dp])**2)