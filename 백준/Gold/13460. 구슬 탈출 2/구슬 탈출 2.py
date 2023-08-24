from collections import deque
n, m = map(int, input().split())
maps = [input() for _ in range(n)]
move = [[-1,0],[1,0],[0,-1],[0,1]]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'R':
            rx, ry = i, j
        elif maps[i][j] == 'B':
            bx, by = i, j
queue = deque([[[rx, ry, bx, by], 0]])
vi = set()
def moving(x, y, dx, dy):
    d = 0
    while maps[x + dx][y + dy] != "#" and maps[x][y] != 'O':
        x, y = x + dx, y + dy
        d += 1
    return x, y, d
def solution():
    while queue:
        pos, cnt = queue.popleft()
        if cnt >= 10: break
        vi.add(tuple(pos))
        rx, ry, bx, by = pos
        for i in range(4):
            nrx, nry, rd = moving(rx, ry, move[i][0], move[i][1])
            nbx, nby, bd = moving(bx, by, move[i][0], move[i][1])
            if maps[nbx][nby] == 'O': continue
            if nrx == nbx and nry == nby:
                if rd > bd:
                    nrx, nry = nrx - move[i][0], nry - move[i][1]
                else:
                    nbx, nby = nbx - move[i][0], nby - move[i][1]
            if maps[nrx][nry] == 'O':
                return cnt + 1
            if tuple([nrx, nry, nbx, nby]) not in vi:
                queue.append([[nrx, nry, nbx, nby], cnt+1])
                vi.add(tuple([nrx, nry, nbx, nby]))
    return -1
print(solution())