maps = [list(map(int, input().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if maps[i][j] == 0:
            zeros.append([i, j])

def row(i, val):
    for j in range(9):
        if maps[i][j] == val:
            return False
    return True

def col(j, val):
    for i in range(9):
        if maps[i][j] == val:
            return False
    return True

def box(i, j, val):
    r, c = 3*(i//3), 3*(j//3)
    for x in range(r, r+3):
        for y in range(c, c+3):
            if maps[x][y] == val:
                return False
    return True
    
def dfs(ind):
    if ind == len(zeros):
        for r in maps:
            print(' '.join(map(str, r)))
        exit(0)
    x, y = zeros[ind]
    for i in range(1, 10):
        if row(x, i) and col(y, i) and box(x,y,i):
            maps[x][y] = i
            dfs(ind+1)
            maps[x][y] = 0
dfs(0)