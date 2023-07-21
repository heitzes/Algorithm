from collections import defaultdict
n = int(input())
likes = [list(map(int, input().split())) for _ in range(n*n)]
slikes = sorted(likes)
sclass = [[0]*n for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
pos = defaultdict(tuple)

def find_empty(coord):
    cnt = 0
    x, y = coord
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<n and sclass[nx][ny] == 0:
            cnt += 1
    return cnt

def find_like(coord):
    cnt = 0
    x, y = coord
    s = sclass[x][y]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<n and sclass[nx][ny] in slikes[s-1]:
            cnt += 1
    return cnt

for s in likes:
    student, like = s[0], s[1:]
    candidates = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if sclass[i][j] == 0:
                candidates[(i,j)] = 0
    for friend in like:
        if friend not in pos: continue
        x, y = pos[friend]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and sclass[nx][ny] == 0:
                candidates[(nx, ny)] += 1
    citems = sorted(list(candidates.items()), key=lambda x: [-x[-1], -find_empty(x[0]), x[0]])
    c = citems[0][0]
    sclass[c[0]][c[1]] = student
    pos[student] = c
    
ans = 0
scores = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
for i in range(n):
    for j in range(n):
        ans += scores[find_like([i, j])]
print(ans)