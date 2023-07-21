import sys
input = sys.stdin.readline

r, c = map(int, input().split())
vi = [0] * 26
board = [list(map(lambda x:ord(x)-65, input())) for _ in range(r)]
vi[board[0][0]] = 1 
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
maxi = 1
def dfs(i, j, cnt):
    global maxi
    maxi = max(maxi, cnt)
    if maxi == 26:
        return maxi
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0<=nx<r and 0<=ny<c:
            if not vi[board[nx][ny]]:
                vi[board[nx][ny]] = 1
                dfs(nx, ny, cnt + 1)
                vi[board[nx][ny]] = 0
    return maxi
print(dfs(0, 0, 1))