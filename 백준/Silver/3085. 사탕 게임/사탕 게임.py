n = int(input())
candy1 = [list(input()) for _ in range(n)]
def count(row):
    maxi, idx = 0, 0
    while idx != len(row)-1:
        cnt, color = 1, row[idx]
        for i in range(idx+1, len(row)):
            if row[i] == color:
                cnt += 1
                continue
            idx = i
            maxi = max(maxi, cnt)
            break
        else:
            return max(maxi, cnt)
    return maxi
maximum = 0
for i in range(n):
    for j in range(n):
        mcolor = candy1[i][j]
        for dx, dy in [[0,1], [1,0]]:
            ni, nj = i+dx, j+dy
            if 0<=ni<n and 0<=nj<n:
                ncolor = candy1[ni][nj]
                if ncolor != mcolor:
                    candy1[i][j], candy1[ni][nj] = ncolor, mcolor
                    for r in candy1:
                        maximum = max(maximum, count(r))
                    for r in list(map(list, zip(*candy1))):
                        maximum = max(maximum, count(r))
                    candy1[i][j], candy1[ni][nj] = mcolor, ncolor
print(maximum)