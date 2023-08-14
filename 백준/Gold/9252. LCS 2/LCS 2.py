str1, str2 = input(), input()
dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
x, y = len(str1), len(str2)
answer = ''
while dp[x][y] != 0:
    if dp[x-1][y] == dp[x][y]:
        x, y = x-1, y
    elif dp[x][y-1] == dp[x][y]:
        x, y = x, y-1
    else:
        answer += str1[x-1]
        x, y = x-1, y-1
print(dp[-1][-1])
if dp[-1][-1] != 0:
    print(answer[::-1])