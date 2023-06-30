import sys
sys.setrecursionlimit(10**6)
n, s, d = map(int, input().split())
graph = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
val = [0 for _ in range(n+1)]
vi = set()
def make_tree(idx):
    vi.add(idx)
    length = 0
    for ch in graph[idx]:
        if ch in vi:
            tree[ch].append(idx)
            continue
        length = max(length, make_tree(ch) + 1)
    val[idx] = length
    return length
answer = 0
make_tree(s)
for v in val[1:]:
    if v >= d: answer += 1
print((answer-1)*2 if answer != 0 else 0)