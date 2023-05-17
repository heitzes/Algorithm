import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
n = int(input())
people = list(map(int, input().split()))
cost = {i: [0, people[i]] for i in range(n)}
graph = defaultdict(list)
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
def make_tree(i):
    tree = defaultdict(list)
    vi, dq = set([i]), deque([i])
    while dq:
        dpop = dq.popleft()
        for ch in graph[dpop]:
            if ch in vi:
                continue
            tree[dpop].append(ch)
            dq.append(ch)
            vi.add(ch)
    return tree
tree = make_tree(0)
def postOrder(node):
    for ch in tree[node]:
        postOrder(ch)
        cost[node][0] += max(cost[ch])
        cost[node][1] += cost[ch][0]
    return cost
print(max(postOrder(0)[0]))