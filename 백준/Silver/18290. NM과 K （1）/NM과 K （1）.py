n, m, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
vi = [[0]*m for _ in range(n)]
dxy = [[0,1], [0,-1], [1,0], [-1,0]]
ans = -1e9
def dfs(i,j,cnt,val):
    global n, m, k, ans
    if cnt == k:
        ans = max(ans, val)
        return
    for x in range(i, n):
        for y in range(j if x==i else 0, m):
            if vi[x][y]: continue
            flag = True
            for a in range(4):
                nx, ny = x + dxy[a][0], y + dxy[a][1]
                if not (0<=nx<n and 0<=ny<m): continue
                if vi[nx][ny] == 1:
                    flag = False
            if flag:
                vi[x][y] = 1
                dfs(x, y, cnt+1, val+maps[x][y])
                vi[x][y] = 0
dfs(0, 0, 0, 0)
print(ans)