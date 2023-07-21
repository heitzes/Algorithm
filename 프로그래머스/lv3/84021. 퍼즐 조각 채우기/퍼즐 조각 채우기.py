from collections import deque
def bfs(arr, vi, dq, mode):
    shape = []
    vi[dq[0][0]][dq[0][1]] = 1
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while dq:
        x, y = dq.popleft()
        shape.append([x, y])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr):
                if not vi[nx][ny] and arr[nx][ny] == mode:
                    vi[nx][ny] = 1
                    dq.append([nx, ny])
    return sorted(shape)
def get_shape(arr, mode):
    n, shape_list = len(arr), []
    vi = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == mode and not vi[i][j]:
                shape_list.append(bfs(arr, vi, deque([[i, j]]), mode))
    return shape_list
def relative(sp):
    new_sp = []
    for sh in sp:
        new_sp.append([[x-sh[0][0], y-sh[0][1]] for x, y in sh])
    return new_sp
def solution(game_board, table):
    """
    감이 안잡혀서 힌트 봄
        1. 조각을 회전하지 말고 보드판을 회전
        2. 같은 조각인지 알기 위해 오름차순으로 정렬한 상대 좌표값을 비교
    테이블의 조각이 회전된 보드판의 조각 중 하나에 들어가게 된다면,
    해당 보드판에 조각을 끼워넣는다
    """
    n = len(game_board)
    vi_table = [[0 for _ in range(n)] for _ in range(n)]
    shape_table, shape_boards = [], []
    shape_table = get_shape(table, 1)
    shape_table = relative(shape_table)
    ans = 0
    for shape in shape_table:
        for i in range(4):
            game_board = list(map(list, zip(*game_board[::-1])))
            shape_board = get_shape(game_board, 0)
            rshape_board = relative(shape_board)
            if shape in rshape_board:
                ind = rshape_board.index(shape)
                find = shape_board[ind]
                ans += len(shape)
                for x, y in find:
                    game_board[x][y] = 1
                break # 중복으로 들어가는 것 피하기 위해
    return ans