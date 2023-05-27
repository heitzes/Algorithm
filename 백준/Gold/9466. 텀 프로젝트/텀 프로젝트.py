import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
t = int(input())

def case(students):
    slen = len(students)
    cycle = set()
    graph = dict()
    for i, s in enumerate(students, 1):
        if i == s: 
            cycle.add(s)
        graph[i] = s
    return cycle, graph

def dfs(nodes, now):
    vi.add(now)
    if graph[now] not in vi:
        vset = dfs(nodes, graph[now])
        if now in vset:
            cycle.update(nodes)
            cycle.add(graph[now])
    nodes.add(graph[now])
    return nodes

for _ in range(t):
    n = int(input())
    nlist = list(map(int, input().split()))
    vi = set()
    cycle, graph = case(nlist)
    for i in range(1, n+1):
        if i not in vi:
            dfs(set(), i)
    print(n - len(cycle))