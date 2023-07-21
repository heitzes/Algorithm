n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
def fill(tp, x, y):
    global n
    if tp == 0:
        if y - 1 >= 0:
            return dp[2][x][y-1] + dp[0][x][y-1]
    elif tp == 1:
        if x - 1 >= 0:
            return  dp[2][x-1][y] + dp[1][x-1][y]
    else:
        if x - 1 >= 0 and y - 1 >= 0 and maps[x-1][y] != 1 and maps[x][y-1] != 1:
            return dp[0][x-1][y-1] + dp[1][x-1][y-1] + dp[2][x-1][y-1]
    return 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1: continue
        dp[2][i][j] += fill(2, i, j)
        dp[1][i][j] += fill(1, i, j)
        dp[0][i][j] += fill(0, i, j)
answer = 0
for i in range(3):
    answer += dp[i][n-1][n-1]
print(answer)