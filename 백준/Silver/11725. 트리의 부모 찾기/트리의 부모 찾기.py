import sys
from collections import defaultdict, deque
input = sys.stdin.readline
n = int(input())
vi = set([1])
dq = deque([1])
graph = defaultdict(list)
parent = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def make_tree():
    while dq:
        dpop = dq.popleft()
        for ch in graph[dpop]:
            if ch not in vi:
                parent[ch] = dpop
                dq.append(ch)
                vi.add(ch)
    return parent
ans = make_tree()
for i in range(2, n+1):
    print(ans[i])