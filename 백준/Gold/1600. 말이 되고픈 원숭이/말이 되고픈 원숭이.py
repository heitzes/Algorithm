from collections import deque
k = int(input())
w, h = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(h)]
vi = [[[1e9]*(k+1) for _ in range(w)] for _ in range(h)]
hx, hy = [1, 1, 2, 2, -1, -1, -2, -2], [2, -2, 1, -1, 2, -2, 1, -1]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
dq = deque([[0, 0, k]])
vi[0][0][k] = 0
while dq:
    x, y, rem = dq.popleft()
    move = vi[x][y][rem]
    if rem > 0:
        for i in range(8):
            nx, ny = x + hx[i], y + hy[i]
            if not (0<=nx<h and 0<=ny<w): continue
            if vi[nx][ny][rem-1] != 1e9: continue
            if maps[nx][ny] == 1: continue
            vi[nx][ny][rem-1] = move + 1
            dq.append([nx, ny, rem-1])
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0<=nx<h and 0<=ny<w): continue
        if vi[nx][ny][rem] != 1e9: continue
        if maps[nx][ny] == 1: continue
        vi[nx][ny][rem] = move + 1
        dq.append([nx, ny, rem])
print(min(vi[h-1][w-1]) if min(vi[h-1][w-1])!=1e9 else -1)