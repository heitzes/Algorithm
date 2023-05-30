from collections import defaultdict
n, m = map(int, input().split())
nlist = [0] + list(map(int, input().split()))
graph = defaultdict(list)
for i in range(1, n+1):
    graph[i].append(nlist[i])
    graph[nlist[i]].append(i)
cp, vi, fi = [0] * (n+1), [0] * (n+1), [0] * (n+1)

components = []
def compo(node):
    cnt = 1
    cp[node] = 1
    for ch in graph[node]:
        if not cp[ch]:
            cnt += compo(ch)
    return cnt

for i in range(1, n+1):
    if not cp[i]:
        components.append(compo(i))

cylist = []
def dfs(node):
    vi[node] = 1
    nxt = nlist[node]
    if vi[nxt]: # 방문한적있음
        if not fi[nxt]: # 사이클 끝나지 않음
            cyc = 1
            while nxt != node:
                nxt = nlist[nxt]
                cyc += 1
            cylist.append(cyc)
    else:
        dfs(nxt)
    fi[node] = 1

for i in range(1, n+1):
    if not vi[i]:
        dfs(i)

ncycle = len(cylist)
clist = [min(m, i) for i in components]
dp = [False] * (m+1)
dp[0] = True
for i in range(1, ncycle+1):
    for w in range(m, -1, -1):
        for k in range(cylist[i-1], clist[i-1]+1): 
            if w >= k:
                dp[w] |= dp[w-k]
for w in range(m, -1, -1):
    if dp[w]:
        print(w)
        break