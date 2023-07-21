n, m, k = map(int, input().split())
notebook = [[0] * m for _ in range(n)]
stickers = []
for _ in range(k):
    r, _ = map(int, input().split())
    mono = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(mono)

def check(sx, sy, sticker):
    for i in range(sx, sx+len(sticker)):
        for j in range(sy, sy+len(sticker[0])):
            if sticker[i-sx][j-sy] == 1 and notebook[i][j] == 1:
                return False
    return True

def put(sticker):
    global n, m
    for i in range(n-len(sticker)+1):
        for j in range(m-len(sticker[0])+1):
            if check(i, j, sticker): 
                return True, i, j
    return False, 0, 0

def attach(sticker):
    global n, m
    rotate = 0
    while rotate < 4:
        r, c = len(sticker), len(sticker[0])
        if n < r or m < c: 
            sticker = list(map(list, zip(*sticker[::-1])))
            rotate += 1
            continue
        av, x, y = put(sticker)
        if not av:
            sticker = list(map(list, zip(*sticker[::-1])))
            rotate += 1
            continue
        for i in range(x, x+r):
            for j in range(y, y+c):
                notebook[i][j] += sticker[i-x][j-y]
        break
for sticker in stickers:
    attach(sticker)
print(sum([sum(row) for row in notebook]))