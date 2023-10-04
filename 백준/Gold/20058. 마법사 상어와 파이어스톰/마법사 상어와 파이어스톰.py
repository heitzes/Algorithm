from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()
n, q = map(int, input().split())
nlist = [list(map(int, input().split())) for _ in range(2**n)]
qlist = list(map(int, input().split()))
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def box(sx, sy, leng):
    newBox = list(map(list, zip(*[nlist[sx+i][sy:sy+leng] for i in range(leng)][::-1])))
    for i in range(leng):
        for j in range(leng):
            nlist[sx+i][sy+j] = newBox[i][j]

def check():
    change = []
    for x in range(2**n):
        for y in range(2**n):
            if nlist[x][y] == 0: continue
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not (0<=nx<2**n and 0<=ny<2**n): continue
                if nlist[nx][ny] > 0: cnt += 1
            if cnt < 3: change.append([x, y])
    for x, y in change:
        nlist[x][y] -= 1
    ice = 0
    for row in nlist:
        ice += sum(row)
    return ice

def bfs(x, y):
    rvi = set()
    rvi.add((x, y))
    dq = deque([[x, y]])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0<=nx<2**n and 0<=ny<2**n): continue
            if nlist[nx][ny] != 0 and (nx, ny) not in rvi:
                dq.append([nx, ny])
                rvi.add((nx, ny))
    vi.update(rvi)
    return len(rvi)

for q in qlist:
    for x in range(0, 2**n, 2**q):
        for y in range(0, 2**n, 2**q):
            box(x, y, 2**q)
    k = check()
else:
    print(k)

vi = set()
maxi = 0
for x in range(2**n):
    for y in range(2**n):
        if nlist[x][y] != 0 and (x, y) not in vi:
            maxi = max(maxi, bfs(x, y))
print(maxi)