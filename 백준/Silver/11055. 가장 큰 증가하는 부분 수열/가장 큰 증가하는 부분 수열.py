n = int(input())
nlist = list(map(int, input().split()))
dp = [0] * (n)
dp[0] = nlist[0]
for i in range(1, n):
    maximum = 0
    for j in range(i):
        if nlist[j] < nlist[i]:
            maximum = max(maximum, dp[j])
    dp[i] += maximum + nlist[i]
print(max(dp))