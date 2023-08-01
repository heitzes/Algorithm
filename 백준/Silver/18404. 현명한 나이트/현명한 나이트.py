from collections import deque
n, m = map(int, input().split())
kx, ky = map(int, input().split())
dp = [[-1]*n for _ in range(n)]
dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]
def bfs():
    global kx, ky
    queue = deque([[kx-1, ky-1]])
    dp[kx-1][ky-1] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if not (0<=nx<n and 0<=ny<n):
                continue
            if dp[nx][ny] == -1:
                dp[nx][ny] = dp[x][y] + 1
                queue.append([nx, ny])
bfs()
for _ in range(m):
    x, y = map(int, input().split())
    print(dp[x-1][y-1])