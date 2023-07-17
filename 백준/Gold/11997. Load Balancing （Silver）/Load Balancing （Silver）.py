n = int(input())
cx, cy = set(), set()
hx, hy = dict(), dict()
cows = []
for _ in range(n):
    x, y = map(int, input().split())
    cx.add(x), cy.add(y)
    cows.append([x, y])
for idx, org in enumerate(sorted(cx)):
    hx[org] = idx
for idx, org in enumerate(sorted(cy)):
    hy[org] = idx
preSum = [[0]*1001 for _ in range(1001)]
countCow = [[0]*1001 for _ in range(1001)]
for cow in cows:
    nx, ny = hx[cow[0]], hy[cow[1]]
    countCow[nx][ny] = 1
for i in range(1000):
    for j in range(1000):
        preSum[i+1][j+1] = preSum[i][j+1] + preSum[i+1][j] - preSum[i][j] + countCow[i][j]
answer = n
for i in range(1001):
    for j in range(1001):
        a = preSum[i][j]
        b = preSum[1000][j] - a
        c = preSum[i][1000] - a
        d = preSum[1000][1000] - (a+b+c)
        answer = min(answer, max(a,b,c,d))
print(answer)