from collections import deque
n, m = int(input()), int(input())
graph = [[] for _ in range(n+1)]
adj = [[0] * (n+1) for _ in range(n+1)]

def bfs(idx):
    vi.add(idx)
    dq = deque([idx])
    while dq:
        dpop = dq.popleft()
        for ch in graph[dpop]:
            if ch not in vi:
                vi.add(ch)
                dq.append(ch)
    return vi

for i in range(1, n+1):
    nlist = list(map(int, input().split()))
    for j in range(n):
        if nlist[j] == 1:
            graph[i].append(j+1)

travel = set(map(int, input().split()))
vlist = []
vi = set()
for i in range(1, n+1):
    ref = set(list(vi)[:])
    if i not in vi:
        vlist.append(bfs(i) - ref)
for route in vlist:
    if travel.issubset(route):
        print("YES")
        break
else:
    print("NO")