n = int(input())
nlist = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i+1, n):
        if nlist[j] < nlist[i]:
            dp[j] = max(dp[j], dp[i] + 1)
print(max(dp))