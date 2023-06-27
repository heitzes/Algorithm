n, m = map(int, input().split())
nlist = [int(input()) for _ in range(n)]
lo, hi = -1, 1000000001

def check(money):
    global m
    ref, cnt = money, 1
    for day in nlist:
        if day > money: return False
        if day <= ref:
            ref -= day
        else:
            cnt += 1
            ref = money - day
    if cnt <= m: return True
    return False

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else:
        lo = mid
print(hi)