def check(board):
    bingo = ["OOO", "XXX"]
    ans = set()
    if board[0] in bingo:
        ans.add(board[0])
    if board[1] in bingo:
        ans.add(board[1])
    if board[2] in bingo:
        ans.add(board[2])
    if board[0][0]+board[1][0]+board[2][0] in bingo:
        ans.add(board[0][0]+board[1][0]+board[2][0])
    if board[0][1]+board[1][1]+board[2][1] in bingo:
        ans.add(board[0][1]+board[1][1]+board[2][1])
    if board[0][2]+board[1][2]+board[2][2] in bingo:
        ans.add(board[0][2]+board[1][2]+board[2][2])
    if board[0][0]+board[1][1]+board[2][2] in bingo:
        ans.add(board[0][0]+board[1][1]+board[2][2])
    if board[0][2]+board[1][1]+board[2][0] in bingo:
        ans.add(board[0][2]+board[1][1]+board[2][0])
    if len(ans) == 0:
        return False, "..."
    elif len(ans) == 1:
        return True, list(ans)[0]
    else:
        return False, list(ans)[0]
    
def solution(board):
    bdict = {"O": 0, "X": 0, ".": 0}
    for i in range(3):
        for j in range(3):
            bdict[board[i][j]] += 1
    success, ch = check(board)
    if success:
        if ch == "OOO":
            if bdict["X"] == bdict["O"] -1:
                return 1
        if ch == "XXX":
            if bdict["O"] == bdict["X"]:
                return 1
    else:
        if ch != "...":
            return 0
        if 0<= bdict["O"] - bdict["X"] <= 1:
            return 1
    return 0