import sys
sys.setrecursionlimit(10**6)
n = int(input())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
def dfs(x, y, graph):
    global r, c, dx, dy
    vi[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0<=nx<r and 0<=ny<c):
            continue
        if not vi[nx][ny] and graph[nx][ny]:
            dfs(nx, ny, graph)
    return 1
for _ in range(n):
    r, c, k = map(int, input().split())
    maps = [[0]*(c) for _ in range(r)]
    for _ in range(k):
        i, j = map(int, input().split())
        maps[i][j] = 1
    answer = 0
    vi = [[0]*(c) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not vi[i][j] and maps[i][j]:
                answer += dfs(i, j, maps)
    print(answer)