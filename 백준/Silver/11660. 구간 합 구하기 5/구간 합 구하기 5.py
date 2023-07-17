import sys
def input():
    return sys.stdin.readline().rstrip()
n, m = map(int, input().split())
nlist = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + nlist[i][j]
for _ in range(m):
    r1, c1, r2, c2 = map(int, input().split())
    print(dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1])