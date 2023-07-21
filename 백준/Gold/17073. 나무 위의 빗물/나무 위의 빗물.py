import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()
n, w = map(int, input().split())
graph = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
vi = set()
def make_tree(idx):
    vi.add(idx)
    for ch in graph[idx]:
        if ch in vi:
            tree[ch].append(idx)
            continue
        make_tree(ch)
make_tree(1)
leaf = 0
for i in range(1, n+1):
    if not len(tree[i]): leaf += 1
print(w/leaf)