from collections import deque
n, s, m = map(int, input().split())
musics = list(map(int, input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1
for i in range(n):
    for j in range(m+1):
        if dp[i][j] != 1: continue
        if j - musics[i] >= 0: 
            dp[i+1][j-musics[i]] = 1
        if j + musics[i] <= m: 
            dp[i+1][j+musics[i]] = 1
answer = -1
for i in range(m+1):
    if dp[-1][i] == 1:
        answer = i
print(answer)