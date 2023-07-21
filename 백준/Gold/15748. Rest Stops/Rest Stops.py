l, n, rj, rb = map(int, input().split())
nlist = [list(map(int, input().split())) for _ in range(n)]
rest = []
ans, maxi = 0, 0
for i in range(n-1, -1, -1):
    if nlist[i][1] > maxi:
        rest.append([i, nlist[i][1]])
        maxi = nlist[i][1]
brest = 0
rest = sorted(rest)
for ind, val in rest:
    m, _ = nlist[ind]
    sj, sb = m * rj, m * rb + brest
    ans += (val * (sj - sb))
    brest += sj-sb
print(ans)