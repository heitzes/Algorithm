from collections import deque
def solution(board):
    """bfs + 시뮬레이션
    현재 위치에서 while 4번 (상하좌우)돌려서
    이동시키고, 멈춰서면 그 위치까지 도착하기위한 최소 이동 횟수 업데이트
    멈춰선 위치가 child가 되어 queue에 들어간다
    """
    r, c = len(board), len(board[0])
    maps = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                sx, sy = i, j
            if board[i][j] == 'G':
                ex, ey = i, j
    dq = deque([[sx, sy, 0]])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    maps[sx][sy] = 1
    def check(i, nx, ny):
        if (i == 0 and ny == c-1) or (i==1 and ny==0) or (i==2 and nx == r-1) or (i==3 and nx==0):
            return True
        return False
    def bfs():
        while dq:
            x, y, cnt = dq.popleft()
            if x == ex and y == ey:
                return cnt
            for i in range(4):
                rx, ry = x, y
                move = 0
                while move < max(r, c):
                    move += 1
                    nx, ny = rx + dx[i], ry + dy[i]
                    if not (0<=nx<r and 0<=ny<c):
                        break
                    # D를 마주함 -> 더는 그 방향으로 가면 안됨
                    if board[nx][ny] == 'D':
                        if not maps[rx][ry]:
                            maps[rx][ry] = cnt + 1
                            dq.append([rx, ry, cnt + 1])
                        break
                    # 벽의 끝을 마주함
                    if check(i, nx, ny):
                        if not maps[nx][ny]:
                            maps[nx][ny] = cnt + 1
                            dq.append([nx, ny, cnt + 1])
                        break
                    rx, ry = nx, ny
                    
    ans = bfs()                         
    if ans != None:
        return ans
    else:
        return -1