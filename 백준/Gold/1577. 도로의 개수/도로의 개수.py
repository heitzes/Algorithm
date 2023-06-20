import sys
n, m = map(int, input().split())

def input():
    return sys.stdin.readline().rstrip()

k = int(input())
dp = [[[-1, 0, 0] for _ in range(m+1)] for _ in range(n+1)]
for _ in range(k):
    a, b, c, d = map(int, input().split())
    coord = sorted([[a, b], [c, d]], key= lambda x: sum(x))
    prev, nxt = coord[0], coord[1]
    dp[nxt[0]][nxt[1]][2 if prev[0]==nxt[0] else 1] = -1

def dfs(x, y):
    if dp[x][y][0] != -1:
        return dp[x][y][0]
    if (x==0 and y==0):
        return 1
    cnt = 0
    if x >= 1 and dp[x][y][1] != -1:
        cnt += dfs(x-1, y)
    if y >= 1 and dp[x][y][2] != -1:
        cnt += dfs(x, y-1)
    dp[x][y][0] = cnt
    return dp[x][y][0]
dfs(n, m)
print(dp[n][m][0])