n, k = int(input()), int(input())
nlist = sorted(set(map(int, input().split())))
ans = 0
def solution():
    global n, k, ans
    if k == 1:
        return nlist[-1] - nlist[0]
    gaps = sorted([[nlist[i]-nlist[i-1], i-1] for i in range(1, len(nlist))])
    cut = sorted(gaps[-k+1:], key= lambda x: x[-1])
    clist = [[] for _ in range(k-1)]
    for i, c in enumerate(cut):
        clist[i] = nlist[cut[i-1][1]+1 if i!=0 else 0:c[1]+1]
    if cut:
        clist.append(nlist[c[1]+1:])
    for center in clist:
        if not center: continue
        ans += center[-1] - center[0]
    return ans
print(solution())