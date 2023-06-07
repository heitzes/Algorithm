n, num = int(input()), int(input())
maps = [[0] * n for _ in range(n)]
sx, sy = n//2, n//2 if n % 2 else n//2-1
cnt = 1
maps[sx][sy] = 1

def printarr(arr):
    for row in arr:
        print(row)
        
for i in range(2, n+1):
    if i % 2:
        sx, sy = sx+1, sy
    else:
        sx, sy = sx-1, sy
    
    if i % 2 == 0:
        for right in range(i):
            cnt += 1
            maps[sx][sy+right] = cnt
        sy += i-1
        for down in range(1, i):
            cnt += 1
            maps[sx+down][sy] = cnt
        sx += i-1
    else:
        for left in range(i):
            cnt += 1
            maps[sx][sy-left] = cnt
        sy -= i-1
        for up in range(1, i):
            cnt += 1
            maps[sx-up][sy] = cnt
        sx -= i-1
for i in range(n):
    for j in range(n):
        if maps[i][j] == num:
            cx, cy = i+1, j+1
for row in maps:
    print(' '.join(map(str, row)))
print(cx, cy)