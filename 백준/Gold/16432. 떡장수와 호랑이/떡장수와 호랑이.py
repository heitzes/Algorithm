import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
nlist = [list(map(int, input().split()))[1:] for _ in range(n)]
dp = [[-1]*10 for _ in range(n)]

anslist = []
def dfs(ind, dduck):
    global n
    if ind == 0 and len(ans)==n:
        anslist.append(tuple(ans))
        return True
    if dp[ind][dduck] != -1:
        return dp[ind][dduck]
    dp[ind][dduck] = False
    for d in range(1, 10):
        if d in nlist[ind-1] and d != dduck:
            ans.append(d)
            dp[ind][dduck] |= dfs(ind-1, d)
            ans.pop()
    return dp[ind][dduck]

for d in nlist[-1]:
    if dp[n-1][d] == -1:
        ans = [d]
        dfs(n-1, d)
        
if not anslist:
    print(-1)
else:
    for s in anslist[0][::-1]:
        print(s)