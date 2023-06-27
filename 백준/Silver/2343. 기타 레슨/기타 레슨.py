from bisect import bisect_right
n, m = map(int, input().split())
nlist = list(map(int, input().split()))
dp = [0] * n
dp[0] = nlist[0]
for i in range(1, n):
    dp[i] = dp[i-1] + nlist[i]
left, right = 0, sum(nlist)

def check(k):
    global m
    ref, cnt = 0, 1
    if max(nlist) > k: return False
    for lecture in nlist:
        if ref + lecture <= k:
            ref += lecture
        else:
            cnt += 1
            ref = lecture
    if cnt > m: return False
    return True 

while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)