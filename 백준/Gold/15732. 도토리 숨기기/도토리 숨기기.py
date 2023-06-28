from bisect import bisect_right
n, k, d = map(int, input().split())
nlist = [list(map(int, input().split())) for _ in range(k)]
nuts = []

def check(num):
    global d
    ans = 0
    for rule in nlist:
        start, end, gap = rule
        if num < start: continue
        ans += (min(end, num) - start)//gap + 1
    if ans >= d: return True
    return False

lo, hi = 0, 1000001
while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid - 1
        answer = mid
    else:
        lo = mid + 1
print(answer)