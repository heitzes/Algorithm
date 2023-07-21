import sys
sys.setrecursionlimit(10**6)
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
minimum = min([min(row) for row in maps])
maximum = max([max(row) for row in maps])
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
answer = 0
def dfs(x, y, k):
    vi[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0<=nx<n and 0<=ny<n): continue
        if not vi[nx][ny] and maps[nx][ny] > k:
            dfs(nx, ny, k)
    return 

for rain in range(minimum-1, maximum):
    vi = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not vi[i][j] and maps[i][j] > rain:
                cnt += 1
                dfs(i, j, rain)
    answer = max(answer, cnt)
print(answer)