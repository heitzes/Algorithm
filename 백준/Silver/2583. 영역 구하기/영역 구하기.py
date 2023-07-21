import sys
sys.setrecursionlimit(10**6)
c, r, k = map(int, input().split())
vi = [[0]*(c) for _ in range(r)]
maps = [[0]*(c) for _ in range(r)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        maps[x][y1:y2] = [1] * (y2-y1)
def dfs(x, y):
    cnt = 1
    vi[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0<=nx<r and 0<=ny<c): continue
        if not vi[nx][ny] and not maps[nx][ny]:
            cnt += dfs(nx, ny)
    return cnt
ans, result = 0, []
for i in range(r):
    for j in range(c):
        if not vi[i][j] and not maps[i][j]:
            ans += 1
            result.append(dfs(i, j))
print(ans)
print(' '.join(map(str, sorted(result))))