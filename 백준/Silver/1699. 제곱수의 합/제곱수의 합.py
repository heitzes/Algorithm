n = int(input())
root = int(n**(0.5))
dp = [i for i in range(n+1)]
for i in range(n+1):
    for j in range(int(i**0.5)+1):
        dp[i] = min(dp[i], dp[i-j*j]+1)
print(dp[n])