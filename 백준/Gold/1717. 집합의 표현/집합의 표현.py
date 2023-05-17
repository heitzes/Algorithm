import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m = map(int, input().split())
uf = [-1] * (n+1)
size = [1] * (n+1)
def find(k):
    if uf[k] < 0:
        return k
    uf[k] = find(uf[k])
    return uf[k]
def union(ra, rb):
    if ra == rb:
        return
    sa, sb = size[ra], size[rb]
    if sa >= sb:
        size[ra] += size[rb]
        uf[rb] = ra
    else:
        size[rb] += size[ra]
        uf[ra] = rb
for _ in range(m):
    mode, a, b = map(int, input().split())
    ra, rb = find(a), find(b)
    if mode == 0:
        union(ra, rb)
    else:
        if ra != rb:
            print("no")
        else:
            print("yes")