nlist = list(map(int, input().split()))
n, percent = nlist[0], nlist[1:]
vi, ans = set([tuple((0,0))]), 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
def dfs(x, y, p, ind):
    global n, ans
    if ind == n:
        ans += p
        return ans
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (nx, ny) not in vi:
            vi.add((nx, ny))
            dfs(nx, ny, p*(percent[i]/100), ind+1)
            vi.remove((nx, ny))
    return ans
print(dfs(0, 0, 1, 0))