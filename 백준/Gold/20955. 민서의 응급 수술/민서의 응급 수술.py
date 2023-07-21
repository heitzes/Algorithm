import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
vi = set()
def make_tree(idx, cnt):
    global edges
    vi.add(idx)
    cnt = 1
    edges += len(graph[idx])
    for ch in graph[idx]:
        if ch in vi:
            tree[ch].append(idx)
            continue
        cnt += make_tree(ch, cnt + 1)
    return cnt
answer = 0
for i in range(1, n+1):
    if i not in vi:
        edges = 0
        nodes = make_tree(i, 0)
        answer += (edges//2 - (nodes-1))
        answer += 1
print(answer-1)