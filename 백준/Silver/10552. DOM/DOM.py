import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import defaultdict
n, m, p = map(int, input().split())
channels = dict()
vi = [0] * (m+1)
for i in range(1, n+1):
    fav, hat = map(int, input().split())
    if hat not in channels:
        channels[hat] = fav
def dfs(node):
    global cnt
    vi[node] = 1
    if node not in channels:
        return cnt
    nxt = channels[node]
    if vi[nxt]:
        return -1
    cnt += 1
    return dfs(nxt)

cnt = 0
print(dfs(p))