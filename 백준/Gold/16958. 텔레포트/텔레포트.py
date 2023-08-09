import sys

n, t = map(int, sys.stdin.readline().rstrip().split())
tele = [0 for _ in range(n)]
pos = [[] for _ in range(n)]
for i in range(n):
    tp, row, col = map(int, sys.stdin.readline().rstrip().split())
    tele[i] = tp
    pos[i] = [row, col]
INF = 10000
dist = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j: dist[i][j] = 0
        else:
            i_pos = pos[i]
            j_pos = pos[j]
            distance = abs(i_pos[0] - j_pos[0]) + abs(i_pos[1] - j_pos[1])
            if tele[i] == 1 and tele[j] == 1 and t < distance: distance = t
            dist[i][j] = distance
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
m = int(input())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    print(dist[s-1][e-1])