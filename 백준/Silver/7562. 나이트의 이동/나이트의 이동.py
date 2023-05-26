from collections import deque

n = int(input())
def bfs(x, y, l):
    dx, dy = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
    dq = deque([[x, y]])
    vi = [[0]*l for _ in range(l)]
    while dq:
        cx, cy = dq.popleft()
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0<=nx<l and 0<=ny<l): continue
            if vi[nx][ny] == 0:
                vi[nx][ny] = vi[cx][cy] + 1
                dq.append([nx, ny])
    return vi


for _ in range(n):
    m = int(input())
    cx, cy = map(int, input().split())
    nx, ny = map(int, input().split())
    if (cx == nx and cy == ny): 
        print(0)
        continue
    print(bfs(cx, cy, m)[nx][ny])