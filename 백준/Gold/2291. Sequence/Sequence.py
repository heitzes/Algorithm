n, m, k = map(int, input().split())
dp = [[[-1 for _ in range(221)] for _ in range(m+1)] for _ in range(n+1)]
def dfs(x, y, num):
    if x == 1:
        dp[1][y][num] = 1
        return 1
    if dp[x][y][num] != -1: return dp[x][y][num]
    dp[x][y][num] = 0
    for i in range(max(1, num), int(y//x)+1):
        dp[x][y][num] += dfs(x-1, y-i, i)
    return dp[x][y][num]
dfs(n, m, 0)
def find(x, y, num, order):
    global n, m, k
    if k == 1 and len(order) == n-1:
        return ' '.join(order + [str(y)])
    for i in range(max(1, num), int(y//x)+1):
        if dp[x-1][y-i][i] >= k:
            return find(x-1, y-i, i, order +[str(i)])
        else:
            k -= dp[x-1][y-i][i]
print(find(n, m, 0, []))