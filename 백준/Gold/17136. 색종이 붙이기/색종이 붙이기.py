maps = [list(map(int, input().split())) for _ in range(10)]
answer = 25
count = [0, 5, 5, 5, 5, 5]
vi = [[0]*10 for _ in range(10)]
cover = 0
for i in range(10):
    for j in range(10):
        cover += maps[i][j]

def printArr(arr):
    for row in arr:
        print(' '.join(map(str, row)))

def max_p(i, j):
    for p in range(1,6):
        for nx in range(i, i+p):
            for ny in range(j, j+p):
                if not (0<=nx<10 and 0<=ny<10): 
                    return p-1
                if maps[nx][ny] == 0: 
                    return p-1
    return p

def dfs(x, y, remain):
    global answer
    if not remain:
        answer = min(answer, 25-sum(count))
        return answer
    for i in range(x, 10):
        for j in range(y if i==x else 0, 10):
            if vi[i][j]: continue
            if not maps[i][j]: continue
            maxp = max_p(i, j)
            for p in range(maxp, 0, -1):
                if count[p] == 0: continue
                if answer < 25-sum(count): break
                vi[i][j] = 1
                count[p] -= 1
                for nx in range(i, i+p):
                    for ny in range(j, j+p):
                        maps[nx][ny] = 0
                dfs(i, j, remain - p*p)
                vi[i][j] = 0
                count[p] += 1
                for nx in range(i, i+p):
                    for ny in range(j, j+p):
                        maps[nx][ny] = 1
            return answer
    return answer
ans = dfs(0, 0, cover)
if ans == 25:
    print(-1)
else:
    print(ans)