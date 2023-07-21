from collections import Counter
t = int(input())
n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))
def make_dp(k, org, dplist):
    for i in org:
        if not dplist: 
            dplist.append(i)
            continue
        dplist.append(dplist[-1] + i)
    cnt = dplist[:]
    for i in range(k):
        for j in range(i+1, k):
            cnt.append(dplist[j] - dplist[i])
    return cnt
ncnt, mcnt = Counter(make_dp(n, nlist, [])), Counter(make_dp(m, mlist, []))
answer = 0
for i in ncnt:
    if t-i in mcnt:
        answer += ncnt[i] * mcnt[t-i]
print(answer)