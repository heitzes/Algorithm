def search(m, n, board):
    coord = set()
    dx, dy = [1, 1, 0], [0, 1, 1]
    for x in range(n-1):
        for y in range(m-1):
            tp = board[x][y]
            if tp == '1':
                continue
            for k in range(3):
                nx, ny = x + dx[k], y + dy[k]
                if nx >= n or ny >= m or board[nx][ny] != tp:
                    break
            else:
                coord.add((x, y))
    return coord
def change(rm, board):
    new_board, cnt = [], 0
    dx, dy = [1, 1, 0], [0, 1, 1]
    for x, y in rm:
        board[x][y] = '0'
        for k in range(3):
            nx, ny = x + dx[k], y + dy[k]
            board[nx][ny] = '0'
    for row in board:
        str_row = ''.join(row)
        str_row = str_row.replace('0', '')
        cnt += (len(row) - len(str_row))
        str_row += '1' * (len(row) - len(str_row))
        new_board.append(list(str_row))
    return new_board, cnt
def solution(m, n, board):
    """
    1. 일단 블록이 제거 되는 방향이 위에서 아래 보단 오른쪽에서 왼쪽이 더 직관적이니까
    board을 90도 돌린다 => 가로가 m, 세로가 n
    2. 보드판 좌표 하나씩 방문하며 오른쪽,아래,대각선 아래가 같은 타입인지 확인하며 블록을 찾는다
    3. 한 블록안의 좌표 중 첫 좌표를 set에 넣는다
    4. [0,0]부터 [m-2, n-2]까지 블록 서치를 마치면, set의 좌표들에 대해 board 값을 0으로 변경
    5. board를 재구성한다 (각 행 별로 0인 값들은 제거, 제거한 수만큼 행의 맨 뒤에 0 붙이기)
    """
    board = list(map(list, zip(*board[::-1])))
    answer = 0
    tri = 0
    while True:
        remove = search(m, n, board)
        board, count = change(remove, board)
        answer += count
        if count == 0:
            break
    
    return answer