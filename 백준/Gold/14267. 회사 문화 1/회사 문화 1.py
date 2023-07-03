import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
parent = list(map(int, input().split()))
mlist = [list(map(int, input().split())) for _ in range(m)]
tree = [[] for _ in range(n+1)]
for i in range(1, n):
    if parent[i] != -1:
        tree[parent[i]].append(i+1)

init = [0] * (n+1)
points = [0] * (n+1)

def spread(idx, pt):
    for ch in tree[idx]:
        spread(ch, pt + init[ch])
    points[idx] = pt

for start, val in mlist:
    init[start] += val
spread(1, 0)
print(' '.join(map(str, points[1:])))