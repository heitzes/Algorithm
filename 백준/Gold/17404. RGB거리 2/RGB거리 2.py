n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9
combination = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]]
def make_dp(comb):
    global n, answer
    dp = [[1e9, 1e9, 1e9] for _ in range(n)]
    dp[0][comb[0]] = nlist[0][comb[0]]
    for i in range(1, n-1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + nlist[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + nlist[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + nlist[i][2]
    for i in range(3):
        if i != comb[1]:
            dp[n-1][comb[1]] = min(dp[n-1][comb[1]], dp[n-2][i] + nlist[n-1][comb[1]])
    answer = min(answer, dp[n-1][comb[1]])
for comb in combination:
    make_dp(comb)
print(answer)