def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    preSum = [[0]*(m+1) for _ in range(n+1)]
    for t, r1, c1, r2, c2, dg in skill:
        k = (-1) ** t * dg
        preSum[r1][c1] += k
        preSum[r1][c2+1] += -k
        preSum[r2+1][c1] += -k
        preSum[r2+1][c2+1] += k
    for i in range(n+1):
        for j in range(1, m+1):
            preSum[i][j] += preSum[i][j-1]
    for j in range(m+1):
        for i in range(1, n+1):
            preSum[i][j] += preSum[i-1][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += preSum[i][j]
            if board[i][j] > 0: answer += 1
    return answer