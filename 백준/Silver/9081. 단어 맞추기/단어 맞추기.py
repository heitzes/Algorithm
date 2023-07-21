n = int(input())
nlist = [[ord(i) for i in list(input())] for _ in range(n)]

def find(ind):
    s, e, comp = -1, -1, 200
    for i in range(len(nlist[ind])-1, -1, -1):
        if e != -1: break
        for j in range(i+1, len(nlist[ind])):
            if nlist[ind][j] > nlist[ind][i]:
                if nlist[ind][j] < comp:
                    comp = nlist[ind][j]
                    s, e = i, j
    return s, e

for ind in range(n):
    s, e = find(ind)
    if e != -1:
        nlist[ind][s], nlist[ind][e] = nlist[ind][e], nlist[ind][s]
        nlist[ind] = nlist[ind][:s+1] + sorted(nlist[ind][s+1:])
    print(''.join([chr(i) for i in nlist[ind]]))