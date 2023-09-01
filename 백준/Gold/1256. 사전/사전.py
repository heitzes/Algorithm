n, m, k = map(int, input().split())
dp = [[0] * (m+1) for _ in range(n+1)]
answer = ''
for i in range(n+1):
    for j in range(m+1):
        if i == j == 0: continue
        if i == 0 or j == 0: dp[i][j] = 1
        else: dp[i][j] = dp[i-1][j] + dp[i][j-1]
def find(x, y, k):
    global answer
    if dp[x][y] < k: return -1
    if k == 1: 
        answer += 'a'*(x) + 'z'*(y)
        return answer
    if dp[x-1][y] >= k:
        answer += 'a'
        find(x-1, y, k)
    else:
        answer += 'z'
        find(x, y-1, k-dp[x-1][y])
    return answer
print(find(n, m, k))