s1 = input()
s2 = input()
dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
x, y = len(s1), len(s2)
answer = ''
while dp[x][y] != 0:
    if dp[x-1][y] == dp[x][y]:
        x, y = x-1, y
    elif dp[x][y-1] == dp[x][y]:
        x, y = x, y-1
    else:
        answer += s1[x-1]
        x, y = x-1, y-1
print(answer[::-1])