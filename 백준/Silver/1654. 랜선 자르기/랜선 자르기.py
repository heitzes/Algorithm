n, m = map(int, input().split())
nlist = [int(input()) for _ in range(n)]
lo, hi = 0, 2**(31)+1

def check(length):
    global m
    cnt = sum([i//length for i in nlist])
    if cnt >= m: return True
    return False

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        lo = mid
    else:
        hi = mid
print(lo)