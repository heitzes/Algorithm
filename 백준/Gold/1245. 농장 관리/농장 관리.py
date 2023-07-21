from collections import deque
n, m = map(int, input().split())
maps, maxi = [], -1
for _ in range(n):
    maps.append(list(map(int, input().split())))
    maxi = max(maxi, max(maps[-1]))
vi = [[0]*(m) for _ in range(n)]
ans = 0
dx, dy = [0, 0, 1, 1, 1, -1, -1, -1], [1, -1, 0, 1, -1, 0, 1, -1]
def bfs(x, y, val):
    global n, m, ans
    vi[x][y] = 1
    dq = deque([[x, y]])
    flag = False
    while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if not (0<=nx<n and 0<=ny<m): continue
            if maps[nx][ny] > val:
                flag = True
            if not vi[nx][ny] and maps[nx][ny] == val:
                vi[nx][ny] = 1
                dq.append([nx, ny])
    if not flag: ans += 1
for i in range(n):
    for j in range(m):
        if not vi[i][j]:
            bfs(i, j, maps[i][j])
print(ans)