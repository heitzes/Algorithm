from collections import deque
def solution(board):
    n = len(board)
    dq = deque([[0, 0, 0, -1]]) # val, prev, x, y
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    costs = [[[1e9]*4 for _ in range(n)] for _ in range(n)]
    costs[0][0] = [0, 0, 0, 0]
    while dq:
        val, x, y, prev = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0<=nx<n and 0<=ny<n): continue
            if board[nx][ny] == 1: continue
            cost = val + (100 if (prev==i or prev==-1) else 600)
            if costs[nx][ny][i] > cost:
                costs[nx][ny][i] = cost
                dq.append([cost, nx, ny, i])
    return min(costs[-1][-1])