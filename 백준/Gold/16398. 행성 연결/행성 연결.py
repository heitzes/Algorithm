n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
costs = []
for i in range(n):
    for j in range(i+1, n):
        costs.append([nlist[i][j], i, j])
costs.sort()
root = [-1] * n

def find(k):
    if root[k] < 0: return k
    root[k] = find(root[k])
    return root[k]

def union(a, b):
    a, b = find(a), find(b)
    if a == b: return
    root[a] = b
answer, cnt = 0, 0
for cost, a, b in costs:
    if cnt == n-1: break
    if find(a) != find(b):
        union(a, b)
        answer += cost
        cnt += 1
print(answer)