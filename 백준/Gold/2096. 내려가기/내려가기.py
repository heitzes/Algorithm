n = int(input())
init = list(map(int, input().split()))
mindp, maxdp = init[:], init[:]
for i in range(1, n):
    one, two, thr = map(int, input().split())
    mindp = [one + min(mindp[0], mindp[1]), two + min(mindp), thr + min(mindp[1], mindp[2])]
    maxdp = [one + max(maxdp[0], maxdp[1]), two + max(maxdp), thr + max(maxdp[1], maxdp[2])]
print(max(maxdp), min(mindp))