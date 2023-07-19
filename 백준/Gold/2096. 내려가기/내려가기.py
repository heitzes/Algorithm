n = int(input())
init = list(map(int, input().split()))
mindp, maxdp = init[:], init[:]
for i in range(1, n):
    one, two, thr = map(int, input().split())
    min0, min1, min2 = mindp
    mindp[0] = min(min0 + one, min1 + one)
    mindp[1] = min(min0 + two, min1 + two, min2 + two)
    mindp[2] = min(min1 + thr, min2 + thr)
    max0, max1, max2 = maxdp
    maxdp[0] = max(max0 + one, max1 + one)
    maxdp[1] = max(max0 + two, max1 + two, max2 + two)
    maxdp[2] = max(max1 + thr, max2 + thr)
print(max(maxdp), min(mindp))