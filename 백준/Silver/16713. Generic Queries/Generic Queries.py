n, m = map(int, input().split())
nlist = list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(n):
    dp[i+1] = dp[i] ^ (nlist[i])
answer = 0
for _ in range(m):
    s, e = map(int, input().split())
    back = (dp[e] & ~dp[s-1]) | (~dp[e] & dp[s-1])
    answer ^= back
print(answer)