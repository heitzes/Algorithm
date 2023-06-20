n = int(input())
nlist = list(map(int, input().split()))
if len(nlist) != 3:
    nlist.extend([0]*(3-len(nlist)))
dp = [[[-1]*(nlist[0]+1) for _ in range(nlist[1]+1)] for _ in range(nlist[2]+1)]
def dfs(s, c, v):
    s, c, v = max(s, 0), max(c, 0), max(v, 0)
    if s==0 and c==0 and v==0:
        return 0
    if dp[s][c][v] != -1:
        return dp[s][c][v]
    cnt = 1e9
    cnt = min(cnt, dfs(s-1, c-3, v-9) + 1)
    cnt = min(cnt, dfs(s-1, c-9, v-3) + 1)
    cnt = min(cnt, dfs(s-3, c-1, v-9) + 1)
    cnt = min(cnt, dfs(s-3, c-9, v-1) + 1)
    cnt = min(cnt, dfs(s-9, c-1, v-3) + 1)
    cnt = min(cnt, dfs(s-9, c-3, v-1) + 1)
    dp[s][c][v] = cnt
    return dp[s][c][v]
s, c, v = nlist[2], nlist[1], nlist[0]
dfs(s, c, v)
print(dp[s][c][v])