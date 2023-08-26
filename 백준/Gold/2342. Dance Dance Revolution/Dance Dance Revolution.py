nlist = list(map(int, input().split()))
nlist.pop()
move = [[1e9, 2, 2, 2, 2], [1e9, 1, 3, 4, 3], [1e9, 3, 1, 3, 4], [1e9, 4, 3, 1, 3], [1e9, 3, 4, 3, 1]]
dp = [[[1e9]*5 for _ in range(5)] for _ in range(len(nlist))]
dp[0][nlist[0]][0] = 2
dp[0][0][nlist[0]] = 2
def solution():
    if not nlist: return 0
    for k in range(1, len(nlist)):
        now = nlist[k]
        for i in range(5):
            for j in range(5):
                if now != j: 
                    dp[k][now][j] = min(dp[k][now][j], dp[k-1][i][j] + move[i][now])
                if now != i: 
                    dp[k][i][now] = min(dp[k][i][now], dp[k-1][i][j] + move[j][now])
    return min([min(row) for row in dp[-1]])
print(solution())