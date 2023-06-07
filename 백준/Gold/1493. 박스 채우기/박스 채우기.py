from collections import defaultdict
l, w, h = map(int, input().split())
n = int(input())
box = defaultdict(int)
ans, maxVolume, volume = 0, 0, l * w * h

for i in range(n):
    p, k = map(int, input().split())
    box[2**p] = k
    maxVolume += ((2**p)**3) * k
box = sorted(list(box.items()), reverse=True)

def solution(i, j, k):
    global ans, maxVolume, volume
    if maxVolume < volume: return -1
    before = 0
    for length, limit in box:
        use = min(limit, (i//length) * (j//length) * (k//length) - (before*8))
        before = before*8 + use
        volume -= (length ** 3) * use
        ans += use
    if volume == 0:    
        return ans
    return -1

print(solution(l, w, h))