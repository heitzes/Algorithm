n = int(input())
nlist = [[0]*58 for _ in range(58)]
cnt = 0
for _ in range(n):
    x, y = input().split(" => ")
    if x != y and not nlist[ord(x)-65][ord(y)-65]:
        nlist[ord(x)-65][ord(y)-65] = 1
        cnt += 1
for k in range(58):
    for i in range(58):
        for j in range(58):
            if i != j and not nlist[i][j] and nlist[i][k] and nlist[k][j]:
                nlist[i][j] = 1
                cnt += 1
print(cnt)
for i in range(58):
    for j in range(58):
        if nlist[i][j]:
            print("{} => {}".format(chr(i+65), chr((j+65))))