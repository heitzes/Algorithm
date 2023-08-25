from bisect import bisect_left
n = int(input())
nlist = list(map(int, input().split()))
lis = [nlist[0]]
index = [0]
for num in nlist[1:]:
    if num > lis[-1]:
        index.append(len(lis))
        lis.append(num)
    else:
        ind = bisect_left(lis, num)
        lis[ind] = num
        index.append(ind)
nlis = len(lis)-1
rlis = []
for i in range(n-1, -1, -1):
    if index[i] == nlis:
        rlis.append(str(nlist[i]))
        nlis -= 1
    if nlis == -1: break
print(len(rlis))
print(' '.join(rlis[::-1]))