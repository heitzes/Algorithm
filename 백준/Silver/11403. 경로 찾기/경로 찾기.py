n = int(input())
maps = [[] for _ in range(n)]
result = [[0] * (n) for _ in range(n)]
for i in range(n):
    tolist = list(map(int, input().split()))
    for j in range(n):
        if tolist[j] == 1:
            maps[i].append(j)
def dfs(prev, node):
    if prev != node:
        vi.append(node)
    for ch in maps[node]:
        if ch not in vi:
            dfs(node, ch)
    return
for i in range(n):
    vi = []
    if i not in vi:
        dfs(i, i)
    for j in vi:
        result[i][j] = 1
for row in result:
    print(' '.join(map(str, row)))