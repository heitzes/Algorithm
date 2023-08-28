n = int(input())
nlist = list(map(int, input().split()))
cdict = {i: 0 for i in nlist}
for num in nlist:
    for i in range(1, int(num ** (0.5))+1):
        x, y = num//i, num //(num//i)
        if num % i == 0:
            if x in cdict:
                cdict[x] += 1
                cdict[num] -= 1
            if x!=y and y in cdict:
                cdict[y] += 1
                cdict[num] -= 1
print(' '.join([str(cdict[i]) for i in nlist]))