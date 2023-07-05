import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()
n, w = map(int, input().split())
graph = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
water = [0] * (n+1)
water[1] = w
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
vi = set()
def make_tree(idx, h):
    global height
    vi.add(idx)
    for ch in graph[idx]:
        if ch in vi:
            tree[ch].append(idx)
            continue
        make_tree(ch, h+1)
make_tree(1, 0)

def spread(idx):
    length = len(tree[idx])
    if not length: return
    for ch in tree[idx]:
        water[ch] = water[idx] / length
    water[idx] = 0

def travel(idx):
    spread(idx)
    for ch in tree[idx]:
        travel(ch)

travel(1)
cnt, ans = 0, 0
for i in range(1, n+1):
    if water[i] > 0: 
        cnt += 1
        ans += water[i]
print(ans/cnt)