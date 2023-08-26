from collections import deque
n, m = map(int, input().split())
nlist = [list(map(int, list(input()))) for _ in range(n)]
vi = [[0]*m for _ in range(n)]
dp = [[0]*m for _ in range(n)]
ans = [[0]*m for _ in range(n)]
p = [[[0,0] for _ in range(m)] for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1 , 0, 0]
def bfs(a, b):
    global n, m
    dq = deque([[a, b]])
    check = set([(a, b)])
    p[a][b] = [a, b]
    vi[a][b] = 1
    cnt = 1
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0<=nx<n and 0<=ny<m): continue
            if vi[nx][ny] != 1 and nlist[nx][ny] == 0:
                dq.append([nx, ny])
                check.add((nx, ny))
                vi[nx][ny] = 1
                p[nx][ny] = [a, b]
                cnt += 1
    for x, y in check:
        dp[x][y] = cnt
for i in range(n):
    for j in range(m):
        if not nlist[i][j] and not vi[i][j]:
            bfs(i, j)
for x in range(n):
    for y in range(m):
        if not nlist[x][y]: continue
        ps = set()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0<=nx<n and 0<=ny<m): continue
            if nlist[nx][ny] == 0:
                ps.add(tuple(p[nx][ny]))
        for i, j in ps:
            ans[x][y] += dp[i][j]
        ans[x][y] += 1
        ans[x][y] %= 10
for row in ans:
    print(''.join([str(i) for i in row]))