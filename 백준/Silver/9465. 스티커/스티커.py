n = int(input())
for _ in range(n):
    m = int(input())
    stickers = []
    dp = [[0, 0, 0] for _ in range(m+1)]
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    stickers = list(map(list, zip(*stickers)))
    for i in range(1, m+1):
        dp[i][0] = max(dp[i-1])
        dp[i][1] = max(dp[i-1][2]+stickers[i-1][0], dp[i-1][0]+stickers[i-1][0])
        dp[i][2] = max(dp[i-1][1]+stickers[i-1][1], dp[i-1][0]+stickers[i-1][1])
    print(max(dp[-1]))