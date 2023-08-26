from collections import deque
n, m = map(int, input().split())
nlist = [list(map(int, list(input()))) for _ in range(n)]
ans = [[0]*m for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1 , 0, 0]
gnum = 1 # 그룹번호
gvi = [[0]*m for _ in range(n)] # 방문여부 겸 그룹번호 기록
gcnt = dict() # 그룹에 속한 node 수 기록
def bfs(i, j):
    global n, m, gnum
    dq = deque([[i, j]])
    gvi[i][j] = gnum
    gcnt[gnum] = gcnt.get(gnum, 0) + 1
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0<=nx<n and 0<=ny<m): continue
            if not nlist[nx][ny] and not gvi[nx][ny]:
                dq.append([nx, ny])
                gvi[nx][ny] = gnum
                gcnt[gnum] += 1
    gnum += 1
for i in range(n):
    for j in range(m):
        if not nlist[i][j] and not gvi[i][j]:
            bfs(i, j)
for x in range(n):
    for y in range(m):
        if not nlist[x][y]: continue
        gcheck = set()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0<=nx<n and 0<=ny<m): continue
            if gvi[nx][ny] and gvi[nx][ny] not in gcheck:
                ans[x][y] += gcnt[gvi[nx][ny]]
                gcheck.add(gvi[nx][ny])
        ans[x][y] = (ans[x][y] + 1) % 10
for row in ans:
    print(''.join([str(i) for i in row]))