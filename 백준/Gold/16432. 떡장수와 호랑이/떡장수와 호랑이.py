import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
nlist = [list(map(int, input().split()))[1:] for _ in range(n)]
dp = [[-1]*10 for _ in range(n+1)]

anslist = []
def dfs(ind, dduck, ans):
    global n
    if ind == 0:
        for s in ans[::-1]:
            print(s)
        exit(0)
    if dp[ind][dduck] != -1:
        return dp[ind][dduck]
    dp[ind][dduck] = False
    for d in nlist[ind-1]:
        if d != dduck:
            dp[ind][dduck] |= dfs(ind-1, d, ans + [d])
    return dp[ind][dduck]
dfs(n, 0, [])
print(-1)