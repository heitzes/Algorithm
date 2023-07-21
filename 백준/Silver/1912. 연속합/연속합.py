n = int(input())
nlist = list(map(int, input().split()))
maxi = -1001
dp = [maxi] + nlist[:]
for i in range(1, n+1):
    dp[i] = max(dp[i-1]+nlist[i-1], nlist[i-1])
    maxi = max(maxi, dp[i])
print(maxi)