from bisect import bisect_left
import sys
def input():
    return sys.stdin.readline()
n = int(input())
nlist = sorted(list(map(int, input().split())))

answer = float('inf')
x, y, z = 0, 0, 0
def findLeft(i, j, ind):
    if ind-1 != i and ind-1 != j:
        return ind-1
    elif ind-2 != i and ind-2 != j:
        return ind-2
    else:
        return ind-3
def findRight(i, j, ind):
    if ind+1 != i and ind+1 != j:
        return ind+1
    elif ind+2 != i and ind+2 != j:
        return ind+2
    else:
        return ind+3
def calc(i, j, ind):
    global answer, x, y, z
    if ind < 0 or ind >= n:
        return
    if abs(nlist[i] + nlist[j] + nlist[ind]) < answer:
        answer = abs(nlist[i] + nlist[j] + nlist[ind])
        x, y, z = i, j, ind
def compare(i, j, val):
    ind = bisect_left(nlist, val*(-1))
    if ind == n: 
        ind = n-1
    if ind != i and ind != j:
        calc(i, j, ind)
    calc(i, j, findRight(i, j, ind))
    calc(i, j, findLeft(i, j, ind))

for i in range(n):
    for j in range(i+1, n):
        compare(i, j, nlist[i]+nlist[j])
print(' '.join(map(str, sorted([nlist[x], nlist[y], nlist[z]]))))