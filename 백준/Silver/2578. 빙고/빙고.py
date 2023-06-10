from collections import defaultdict
maps = [list(map(int, input().split())) for _ in range(5)]
coord = defaultdict(list)
for i in range(5):
    for j in range(5):
        coord[maps[i][j]] = [i, j]
calls = []
for _ in range(5):
    calls.extend(map(int, input().split()))
    
def check():
    cnt = 0
    for row in maps:
        if sum(row) == 0:
            cnt += 1
    for i in range(5):
        if sum([maps[j][i] for j in range(5)]) == 0:
            cnt += 1
    cross1 = [maps[i][i] for i in range(5)]
    if sum(cross1) == 0:
        cnt += 1
    cross2 = [maps[i][4-i] for i in range(5)]
    if sum(cross2) == 0:
        cnt += 1
    return cnt

answer = 0
while calls:
    num = calls.pop(0)
    answer += 1
    x, y = coord[num]
    maps[x][y] = 0
    if check() >= 3:
        break
print(answer)