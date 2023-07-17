import sys
def input():
    return sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    n, nlist = int(input()), list(map(int, input().split()))
    dp = [0] * n
    for i in range(n):
        dp[i] = max(dp[i-1]+nlist[i], nlist[i])
    print(max(dp))