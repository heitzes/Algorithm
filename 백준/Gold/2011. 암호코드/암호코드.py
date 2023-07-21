n = list(map(int, list(input())))
dp = [[0, 0] for _ in range(len(n))]
dp[0][0] = 1 if n[0] != 0 else 0
for i in range(1, len(n)):
    if n[i] != 0:
        dp[i][0] = sum(dp[i-1])
    if n[i-1] == 1 or n[i-1] == 2 and n[i] <= 6:
        dp[i][1] = dp[i-1][0]
print(sum(dp[-1]) % 1000000)