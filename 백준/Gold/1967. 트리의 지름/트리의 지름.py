import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = [[] for _ in range(n+1)]
tree1 = [[] for _ in range(n+1)]
tree2 = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
vi1 = set()
vi2 = set()
lens1 = [0 for _ in range(n+1)]
lens2 = [0 for _ in range(n+1)]
def make_tree(tree, lens, vi, idx, length):
    vi.add(idx)
    for ch, val in graph[idx]:
        if ch in vi:
            tree[ch].append(idx)
            continue
        make_tree(tree, lens, vi, ch, length + val)
    lens[idx] = length
make_tree(tree1, lens1, vi1, 1, 0)
root = lens1.index(max(lens1))
make_tree(tree2, lens2, vi2, root, 0)
print(max(lens2))