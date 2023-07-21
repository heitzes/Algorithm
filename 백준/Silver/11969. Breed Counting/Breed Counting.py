import sys
def input():
    return sys.stdin.readline().rstrip()
n, m = map(int, input().split())
dp = [[0]*(n+1) for _ in range(3)]
for i in range(n):
    s = int(input())
    dp[s-1][i+1] = 1
for i in range(3):
    for j in range(n):
        dp[i][j+1] += dp[i][j]
for _ in range(m):
    s, e = map(int, input().split())
    print("{} {} {}".format(dp[0][e] - dp[0][s-1], dp[1][e] - dp[1][s-1], dp[2][e] - dp[2][s-1]))