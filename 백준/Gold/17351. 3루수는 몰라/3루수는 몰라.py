import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
maps = [input() for _ in range(n)]
dp = [[[-1]*4 for _ in range(n)] for _ in range(n)]
word = "MOLA"
dx, dy  = [0, 1], [1, 0]
def dfs(x, y, ind):
    global n
    if not (0<=x<n and 0<=y<n): return 0
    if x == n-1 and y == n-1:
        if maps[x][y] == word[ind] == "A": return 1
        return 0
    if dp[x][y][ind] != -1: 
        return dp[x][y][ind]
    if maps[x][y] == word[ind]:
        if ind != 3:
            dp[x][y][ind] = max(dfs(x+1, y, ind+1), dfs(x, y+1, ind+1))
        else:
            dp[x][y][ind] = max(dfs(x+1, y, 0)+1, dfs(x, y+1, 0)+1)
    else:
        if maps[x][y] == "M":
            dp[x][y][ind] = max(dfs(x+1, y, 1), dfs(x, y+1, 1))
        else:
            dp[x][y][ind] = max(dfs(x+1, y, 0), dfs(x, y+1, 0))
    return dp[x][y][ind]
dfs(0, 0, 0)
print(max(0, max(dp[0][0])))