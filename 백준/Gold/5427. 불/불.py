from collections import deque
t = int(input())
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(sang, fires):
    global w, h
    while sang:
        flen = len(fires)
        for _ in range(flen):
            fx, fy = fires.popleft()
            for i in range(4):
                nfx, nfy = fx + dxy[i][0], fy + dxy[i][1]
                if (0<=nfx<h and 0<=nfy<w):
                    if not vif[nfx][nfy] and maps[nfx][nfy] != "#":
                        maps[nfx][nfy] = "*"
                        fires.append([nfx, nfy])
                        vif[nfx][nfy] = 1
        slen = len(sang)
        for _ in range(slen):
            sx, sy = sang.popleft()
            for i in range(4):
                nsx, nsy = sx + dxy[i][0], sy + dxy[i][1]
                if (0<=nsx<h and 0<=nsy<w):
                    if vis[nsx][nsy] == -1 and maps[nsx][nsy] == ".":
                        sang.append([nsx, nsy])
                        vis[nsx][nsy] = vis[sx][sy] + 1
                else:
                    return vis[sx][sy] + 1
    return -1
    
for _ in range(t):
    w, h = map(int, input().split())
    maps = [list(input()) for _ in range(h)]
    vif = [[0]*w for _ in range(h)]
    vis = [[-1]*w for _ in range(h)]
    sang, fires = deque([]), deque([])
    for i in range(h):
        for j in range(w):
            if maps[i][j] == "@":
                sang.append([i, j])
                vis[i][j] = 0
            if maps[i][j] == "*":
                fires.append([i, j])
                vif[i][j] = 1
    ans = bfs(sang, fires)
    print(ans if ans!=-1 else "IMPOSSIBLE")