from itertools import product
n, m = map(int, input().split())
maps = [input() for _ in range(n)]
bmaps = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if maps[i][j] == '.' or maps[i][j] == 'O':
            bmaps[i][j] = 0
        else:
            bmaps[i][j] = 1
        if maps[i][j] == 'R':
            rx, ry = i, j
        elif maps[i][j] == 'B':
            bx, by = i, j
        elif maps[i][j] == 'O':
            ex, ey = i, j
rbmaps = [row[:] for row in bmaps]
move = [[-1,0],[1,0],[0,-1],[0,1]]
def order(rx, ry, bx, by, p):
    x1, y1, x2, y2 = rx, ry, bx, by
    c1, c2 = 'r', 'b'
    if p == 0:
        if ry == by:
            if rx > bx: 
                x1, y1, x2, y2 = bx, by, rx, ry
                c1, c2 = 'b', 'r'
    elif p == 1:
        if ry == by:
            if rx < bx:
                x1, y1, x2, y2 = bx, by, rx, ry
                c1, c2 = 'b', 'r'
    elif p == 2:
        if rx == bx:
            if ry > by:
                x1, y1, x2, y2 = bx, by, rx, ry
                c1, c2 = 'b', 'r'
    else:
        if rx == bx:
            if ry < by:
                x1, y1, x2, y2 = bx, by, rx, ry
                c1, c2 = 'b', 'r'
    return x1, y1, x2, y2, c1, c2

def moving(p):
    global pos
    rx, ry, bx, by = pos
    # print("moving: ", p, rx, ry, bx, by)
    x1, y1, x2, y2, c1, c2 = order(rx, ry, bx, by, p)
    bmaps[x1][y1] = 0

    # 첫 구슬 이동
    bflag1, rflag1 = False, False
    while True:
        nx, ny = x1 + move[p][0], y1 +  move[p][1]
        if maps[nx][ny] == 'O':
            if c1 == 'b': # 파란색 들어감
                bflag1 = True
                break
            else:
                rflag1 = True
        if bmaps[nx][ny] != 1:
            x1, y1 = nx, ny
            continue
        break
    if bflag1:
        return False, 0
    if maps[x1][y1] != 'O':
        bmaps[x1][y1] = 1

    # 두번째 구슬 이동
    bmaps[x2][y2] = 0
    bflag2, rflag2 = False, False
    while True:
        nx, ny = x2 + move[p][0], y2 +  move[p][1]
        if maps[nx][ny] == 'O':
            if c2 == 'b': # 파란색 들어감
                bflag2 = True
                break
            else:
                rflag2 = True
        if bmaps[nx][ny] != 1:
            x2, y2 = nx, ny
            continue
        break
    if bflag2:
        return False, 0
    if maps[x2][y2] != 'O':
        bmaps[x2][y2] = 1

    if c1 == 'b': bx, by = x1, y1
    elif c1 == 'r': rx, ry = x1, y1
    if c2 == 'b': bx, by = x2, y2
    elif c2 == 'r': rx, ry = x2, y2
    pos = [rx, ry, bx, by]
    # print(bx, by, rx, ry)
    # 파란색 안들어감, 빨간색 안들어감
    if not rflag1 and not rflag2:
        return True, 0
    # 파란색 안들어감, 빨간색 들어감
    # print("RED")
    return True, 1

answer = 1e9
def calc(pos, pr):
    rx, ry, bx, by = pos
    # print("calc:", rx, ry, bx, by)
    cnt = 0
    for p in pr:
        res, cont = moving(p)
        if not res: 
            return -1
        cnt += 1
        if res and cont:
            return cnt
    return -1

rrx, rry, rbx, rby = rx, ry, bx, by
cnt = 0
for p in product(range(4), repeat=10):
    pos = [rrx, rry, rbx, rby]
    bmaps = [row[:] for row in rbmaps]
    # print(p)
    ans = calc(pos, p)
    # if ans == 1: print(p)
    if ans != -1: 
        answer = min(answer, ans)
    # for row in bmaps:
    #     print(row)
    # cnt += 1
    # if cnt == 3:
    #     break
print(answer if answer != 1e9 else -1)
# print("c:", calc(rrx, rry, rbx, rby, (3, 3, 3, 3, 3, 3, 3, 3, 3, 3)))
# for row in bmaps:
#     print(row)