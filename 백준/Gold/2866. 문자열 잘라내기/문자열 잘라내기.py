from collections import deque
r, c = map(int, input().split())
words = [input() for _ in range(r)]
words = list(map(list, zip(*words[::-1])))
lo, hi = 0, r
def check(idx):
    cset = set()
    for word in words:
        w = ''.join(word[:idx])
        if w not in cset:
            cset.add(w)
        else: return False
    return True

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else:
        lo = mid
print(r-hi)