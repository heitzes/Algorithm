n = input()
dp = [0] * 41
dp[0], dp[1] = 1, 1 if 1 <= int(n[0]) <= 34 else 0
for i in range(1, len(n)):
    if n[i] != '0':
        dp[i+1] += dp[i]
    if '1' <= n[i-1:i+1] <= '34':
        dp[i+1] += dp[i-1]
print(dp[len(n)])