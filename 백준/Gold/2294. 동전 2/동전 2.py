n, k = map(int, input().split())
money = set()
for _ in range(n):
    money.add(int(input()))
money = sorted(money)
dp = [1e9] * (200001)
dp[0] = 0
for i in range(k-min(money)+1):
    for coin in money:
        dp[i+coin] = min(dp[i+coin], dp[i]+1)
if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])