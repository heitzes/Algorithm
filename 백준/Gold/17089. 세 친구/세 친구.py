n, m = map(int, input().split())
friends = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a][b] = 1
    friends[b][a] = 1
answer = 1e9
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if friends[i][j]:
            for k in range(j+1, n+1):
                if friends[i][k] and friends[j][k]:
                    answer = min(answer, sum(friends[i])+sum(friends[j])+sum(friends[k]))
if answer != 1e9:
    print(answer - 6)
else:
    print(-1)