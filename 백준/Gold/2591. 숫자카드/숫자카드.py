nlist = input()
dp = [0] * (41)
dp[0], dp[1] = 1, 1 if 1 <= int(nlist[0]) <= 34 else 0
for i in range(1, len(nlist)):
    if '1' <= (nlist[i-1]+nlist[i]) <= '34':
        dp[i+1] += dp[i-1]
    if nlist[i] != '0':
        dp[i+1] += dp[i]
print(dp[len(nlist)])