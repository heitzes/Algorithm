n = int(input())
dp = [0] * (n+2)
dp[0], dp[2] = 1, 3
for i in range(4, n+1, 2):
    dp[i] += 3 * dp[i-2]
    dp[i] += sum([2 * dp[i-2*j] for j in range(2, i//2+1)])
if n == 1: print(0)
else: print(dp[n])