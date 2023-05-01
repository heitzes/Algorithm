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
    def bfs():
        vi = set((sx, sy))
        while dq:
            x, y, cnt = dq.popleft()
            if x == ex and y == ey:
                return cnt
            if (x, y) in vi:
                continue
            vi.add((x,y))
            for i in range(4):
                rx, ry = x, y
                while True:
                    nx, ny = rx + dx[i], ry + dy[i]
                    if 0<=nx<r and 0<=ny<c and board[nx][ny] != "D":
                        rx, ry = nx, ny
                        continue
                    dq.append([rx, ry, cnt+1])
                    break
        return -1
    return bfs()