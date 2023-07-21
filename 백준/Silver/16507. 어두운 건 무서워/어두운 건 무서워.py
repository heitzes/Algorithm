import sys
def input():
    return sys.stdin.readline().rstrip()
r, c, q = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(r)]
preSum = [[0]*(c+1) for _ in range(r+1)]
for i in range(r):
    for j in range(c):
        preSum[i+1][j+1] = preSum[i+1][j] + preSum[i][j+1] - preSum[i][j] + maps[i][j]
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    light = (preSum[r2][c2] - preSum[r2][c1-1] - preSum[r1-1][c2] + preSum[r1-1][c1-1])
    print(light // ((r2-r1+1)*(c2-c1+1)))