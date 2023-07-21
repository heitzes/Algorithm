n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
def bino(a, b):
    if dp[a][b] != 0:
        return dp[a][b]
    if b == 0: return 1
    if b == 1: return a
    if b == a: return 1
    dp[a][b] =  bino(a-1, b) + bino(a-1, b-1)
    return dp[a][b]
print(bino(n, k) % 10007)