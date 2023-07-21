n = int(input())
candy1 = [list(input()) for _ in range(n)]
def count(row):
    maxi, cnt = 1, 1
    for idx in range(len(row)-1):
        if row[idx] == row[idx+1]:
            cnt += 1
        else:
            cnt = 1
        maxi = max(cnt, maxi) # 코드를 단순하게 만들기 위해 조금 비효율적으로 짜도 괜찮다.
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