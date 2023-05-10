from collections import deque
def bfs(miro, x, y, mode):
    dq = deque([[x,y,0]])
    vi = set()
    while dq:
        px, py, c = dq.popleft()
        if miro[px][py] == mode:
            return c
        for move in [[0,1], [0,-1], [1,0], [-1,0]]:
            cx, cy = px + move[0], py + move[1]
            if 0<=cx<len(miro) and 0<=cy<len(miro[0]):
                if (cx, cy) not in vi and miro[cx][cy] != "X":
                    dq.append([cx, cy, c+1])
                    vi.add((cx, cy))
    return -1
def solution(maps):
    answer = 0
    lmaps, emaps = maps[:], maps[:]
    r, c = len(maps), len(maps[0])
    for i in range(r):
        for j in range(c):
            if maps[i][j] == "S":
                sx, sy = i, j
            elif maps[i][j] == "L":
                lx, ly = i, j
            elif maps[i][j] == "E":
                ex, ey = i, j
    smove = bfs(lmaps, sx, sy, "L")
    lmove = bfs(emaps,lx, ly, "E")
    if smove == -1 or lmove == -1:
        return -1
    return smove + lmove