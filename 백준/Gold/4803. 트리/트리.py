import sys
input = sys.stdin.readline
def find(k):
    if uf[k] < 0:
        return k
    uf[k] = find(uf[k])
    return uf[k]
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        cycle.add(ra)
        return 
    if rb > ra:
        uf[ra] = rb
    else:
        uf[rb] = ra
commands, order = [], 1
while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    commands.append([a, b])
while commands:
    v, e = commands.pop(0)
    cnt = 0
    uf = [-1] * (v+1)
    cycle = set()
    for i, j in commands[:e]:
        union(i, j)
    cycle = set([find(i) for i in cycle])
    for k in range(1, v+1):
        if uf[k]==-1 and k not in cycle:
            cnt += 1
    commands = commands[e:]
    if cnt == 0:
        print("Case {}: No trees.".format(order))
    if cnt == 1:
        print("Case {}: There is one tree.".format(order))
    if cnt > 1:
        print("Case {}: A forest of {} trees.".format(order, cnt))
    order += 1