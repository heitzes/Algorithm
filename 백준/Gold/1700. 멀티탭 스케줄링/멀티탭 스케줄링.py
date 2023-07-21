from bisect import bisect_right
from collections import defaultdict
n, k = map(int, input().split())
nlist = list(map(int, input().split()))
using, idict = set(), defaultdict(list)
ans = 0
for i in range(k):
    idict[nlist[i]].append(i)
for i, v in enumerate(nlist):
    if v in using: continue
    if len(using) < n: 
        using.add(v) 
        continue
    for u in using:
        if idict[u][-1] < i:
            upop = u
            break
    else:
        upop = max([idict[j][bisect_right(idict[j], i)], j] for j in using)[1]
    using.remove(upop)
    using.add(v)
    ans += 1
print(ans)