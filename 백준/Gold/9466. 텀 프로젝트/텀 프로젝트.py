import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
t = int(input())

def dfs(node):
    global cnt
    vi[node] = 1
    nxt = nlist[node]
    if vi[nxt]:
        if not fi[nxt]:
            start = node
            while nxt != start:
                nxt = nlist[nxt]
                cnt += 1
            cnt += 1
    else: dfs(nlist[node])
    fi[node] = 1

for _ in range(t):
    n = int(input())
    nlist = [0] + list(map(int, input().split()))
    vi = [0] * (n+1)
    fi = [0] * (n+1)
    cnt = 0
    for i in range(1, n+1):
        if not vi[i]: dfs(i)
    print(n - cnt)