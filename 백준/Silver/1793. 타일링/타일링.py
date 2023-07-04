nlist = []
while True:
    try: 
        nlist.append(int(input()))
    except:
        break
dp = [0] * (max(nlist)+1)
dp[0], dp[1], dp[2] = 1, 1, 3
for n in nlist:
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2 * dp[i-2]
    print(dp[n])