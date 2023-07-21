import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
graph = defaultdict(set)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
dp = [[1, 0] for _ in range(n+1)]
vi = set([1])
def postOrder(node):
    for ch in graph[node]:
        if ch in vi:
            continue
        vi.add(ch)
        postOrder(ch)
        dp[node][0] += min(dp[ch])
        dp[node][1] += dp[ch][0]
    return dp
print(min(postOrder(1)[1]))