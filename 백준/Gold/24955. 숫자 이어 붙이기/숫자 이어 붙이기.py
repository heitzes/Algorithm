n, q = map(int, input().split())
nlist = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
tree =[[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def backtrack(idx, num):
    global ans
    if idx == e:
        ans = int(''.join([str(i) for i in num])) % 1000000007
        return num
    vi.add(idx)
    for ch in graph[idx]:
        if ch in vi:
            continue
        num.append(nlist[ch-1])
        backtrack(ch, num)
        num.pop()
    vi.remove(idx)
for _ in range(q):
    s, e = map(int, input().split())
    ans, vi = 0, set()
    backtrack(s, [nlist[s-1]])
    print(ans)