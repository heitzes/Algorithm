"""
column별로 땅과의 거리를 재고, 그 최소값을 찾는다
그 값만큼 유성을 아래로 이동시킨다
"""
r, c = map(int, input().split())
maps = [list(input()) for _ in range(r)]
rmaps =list(map(list, zip(*maps[::-1])))
def distance():
    global r, c
    mini = r + 1
    for i in range(c):
        if 'X' in rmaps[i]:
            s = r - rmaps[i][::-1].index("#")
            x = rmaps[i].index("X")
            mini = min(mini, x-s)
    return mini
move = distance()
def remake(m):
    nmaps = []
    for i in range(c):
        if 'X' in rmaps[i]:
            row = []
            d = rmaps[i][::-1].index("X")
            x1, x2 = rmaps[i].index("X"), r - rmaps[i][::-1].index("X")
            s1, s2 = rmaps[i].index("#"), r - rmaps[i][::-1].index("#")
            row.extend(rmaps[i][s1:s2])
            row.extend(['.'] * (r-(x2-x1)-(s2-s1)-d-m))
            row.extend(rmaps[i][x1:x2])
            row.extend(['.'] * (m+d))
        else:
            row = rmaps[i]
        nmaps.append(row)
    return nmaps
nmaps = list(map(list, zip(*remake(move))))[::-1]
for row in nmaps:
    print(''.join(row))