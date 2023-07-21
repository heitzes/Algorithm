n, atk = map(int, input().split())
nlist = [list(map(int, input().split())) for _ in range(n)]
lo, hi = 0, 123456 * (10**12) + 1

def check(hp):
    global atk
    mhp, chp, catk = hp, hp, atk
    for room in nlist:
        info, a, h = room
        if info == 2:
            catk += a
            chp = min(mhp, chp+h)
            continue
        p = -int(-h//catk) # 몬스터 죽이기
        m = -int(-chp//a) # 용사 죽이기
        if m < p: return False
        chp -= (p-1) * (a)
    return True

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else:
        lo = mid
print(hi)