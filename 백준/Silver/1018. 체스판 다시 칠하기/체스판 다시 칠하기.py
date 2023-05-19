n, m = map(int, input().split())
board = [input() for _ in range(n)]
white = ['WBWBWBWB' if i % 2 == 0 else 'BWBWBWBW' for i in range(8)]
black = ['BWBWBWBW' if i % 2 == 0 else 'WBWBWBWB' for i in range(8)]
def make_board(a, b):
    new_board = []
    for i in range(a, a + 8):
        new_board.append(board[i][b:b+8])
    return new_board
def compare(arr):
    wh, bl = 0, 0
    for i in range(8):
        for j in range(8):
            if arr[i][j] != white[i][j]:
                wh += 1
            if arr[i][j] != black[i][j]:
                bl += 1
    return min(wh, bl)
minimum = 1e9
for i in range(n-7):
    for j in range(m-7):
        cut = make_board(i, j)
        minimum = min(compare(cut), minimum)
print(minimum)