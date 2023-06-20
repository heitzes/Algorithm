n, m, k = map(int, input().split())
words = [list(input()) for _ in range(n)]
starts = []
word = input()

for i in range(n):
    for j in range(m):
        if words[i][j] == word[0]:
            starts.append([i, j])

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
def dfs(x, y, ind):
    global n, m, k
    if ind == len(word)-1:
        return 1
    if dp[x][y][ind] != -1:
        return dp[x][y][ind]
    cnt = 0
    for i in range(4):
        nx, ny = x, y
        for j in range(k):
            nx, ny = nx + dx[i], ny + dy[i]
            if (0<=nx<n and 0<=ny<m) and word[ind+1] == words[nx][ny]:
                cnt += dfs(nx, ny, ind+1)
    dp[x][y][ind] = cnt
    return dp[x][y][ind]

answer = 0
dp = [[[-1]*len(word) for _ in range(m)] for _ in range(n)]
for x, y in starts:
    answer += dfs(x, y, 0)
print(answer)