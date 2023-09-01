string = input()
alpha = set([str(i) for i in range(1, 27)])
dp = [0] * (len(string)+1)
dp[0] = 1 ### 초기값 설정 !!!!
for i in range(1, len(string)+1):
    for j in range(1, 3):
        if i - j < 0 : continue
        if string[i-j:i] in alpha:
            dp[i] += dp[i-j]
print(dp[-1] % 1000000)