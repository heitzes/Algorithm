import bisect
n = int(input())
nlist = sorted(list(map(int, input().split())))
dp = [nlist[0]]
diff, answer = 1e9, 1e9
for i in range(1, n):
    dp.append(dp[-1]+nlist[i])
for num in nlist:
    left = bisect.bisect_left(nlist, num)
    right = bisect.bisect_right(nlist, num)
    ldiff, rdiff = 0, 0
    if left != 0:
        ldiff = num * left - dp[left-1]
    if right != n:
        rdiff = (dp[-1] - dp[right-1]) - num * (n - right) 
    cdiff = ldiff + rdiff
    if cdiff < diff:
        diff = cdiff
        answer = num
print(answer)