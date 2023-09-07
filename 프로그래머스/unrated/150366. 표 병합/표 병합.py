def solution(commands):
    answer = []
    r, c = 50, 50
    board = [['']*(c+1) for _ in range(r+1)]
    p = [[[i, j] for j in range(c+1)] for i in range(r+1)]
    def find(x, y):
        if p[x][y] == [x, y]: return p[x][y]
        rx, ry = p[x][y]
        p[x][y] = find(rx, ry)
        return p[x][y]
    def union(x1, y1, x2, y2):
        rx1, ry1 = find(x1, y1)
        rx2, ry2 = find(x2, y2)
        if rx1==rx2 and ry1==ry2: return
        if board[rx1][ry1]:
            p[rx2][ry2] = [rx1, ry1]
        else:
            p[rx1][ry1] = [rx2, ry2]
    def update(x, y, k):
        rx, ry = find(x, y)
        board[rx][ry] = k
    def updateV(k, v):
        for x in range(1, r+1):
            for y in range(1, c+1):
                rx, ry = find(x, y)
                if board[rx][ry] == k:
                    board[rx][ry] = v
    def dunion(x, y):
        rx, ry = find(x, y)
        string = board[rx][ry]
        reset = []
        for i in range(1, r+1):
            for j in range(1, c+1):
                if find(i, j) == [rx, ry]:
                    reset.append([i, j])
        for i, j in reset:
            p[i][j] = [i, j]
            board[i][j] = ''
        board[x][y] = string
    def printV(x, y):
        rx, ry = find(x, y)
        if board[rx][ry] !='': return board[rx][ry]
        else: return "EMPTY"
    for cmds in commands:
        clist = cmds.split()
        if clist[0] == 'UPDATE':
            if len(clist) == 4:
                update(int(clist[1]), int(clist[2]), clist[3])
            else: updateV(clist[1], clist[2])
        elif clist[0] == "MERGE":
            union(int(clist[1]), int(clist[2]), int(clist[3]), int(clist[4]))
        elif clist[0] == "UNMERGE":
            dunion(int(clist[1]), int(clist[2]))
        elif clist[0] == "PRINT":
            answer.append(printV(int(clist[1]),int(clist[2])))
    return answer