n, k = map(int, input().split())
eat = list(map(int, input().split()))
dp = [0] * (n)
dp[0] = eat[0]
for i in range(1, n):
    if dp[i-1] < k:
        dp[i] = dp[i-1] + eat[i]
    else:
        if eat[i-1] < k:
            dp[i] = eat[i-1] + eat[i]
        else:
            dp[i] = eat[i]
dp.append(k)
change = []
for i, j in zip(dp, dp[1:]):
    if i < j:
        change.append(1)
    else:
        change.append(0)
ans = 0
for i in range(1, len(change)):
    if change[i-1] and not change[i]:
        ans += (dp[i]-k)
if n == 1:
    print(max(eat[0]-k, 0))
else:
    print(ans)