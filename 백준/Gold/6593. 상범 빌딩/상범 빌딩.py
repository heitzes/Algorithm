from collections import deque

def bfs(x, y, z):
    global l, r, c
    dq = deque([[x, y, z]])
    vi[x][y][z] = 0
    while dq:
        x, y, z = dq.popleft()
        for i in range(6):
            nx, ny, nz = x + dxyz[i][0], y + dxyz[i][1], z + dxyz[i][-1]
            if (0<=nx<l and 0<=ny<r and 0<=nz<c):
                if maps[nx][ny][nz] != '#' and vi[nx][ny][nz] == -1:
                    vi[nx][ny][nz] = vi[x][y][z] + 1
                    dq.append([nx, ny, nz])
    return vi

while True:
    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        break
    maps = []
    vi = [[[-1]*c for _ in range(r)] for _ in range(l)]
    dxyz = [[1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0]]
    for _ in range(l): 
        floor = [input() for _ in range(r)]
        maps.append(floor)
        input()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if maps[i][j][k] == "S":
                    sl, sr, sc = i, j, k
                if maps[i][j][k] == "E":
                    el, er, ec = i, j, k
    visited = bfs(sl, sr, sc)
    if visited[el][er][ec] == -1:
        print("Trapped!")
    else:
        print("Escaped in {} minute(s).".format(visited[el][er][ec]))