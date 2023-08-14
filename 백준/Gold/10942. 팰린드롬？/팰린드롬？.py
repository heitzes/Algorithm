import sys
def input():
    return sys.stdin.readline()
n = int(input())
nlist = list(map(int, input().split()))
pel = [[0]*(n) for _ in range(n)]
for length in range(1, n+1):
    for i in range(n-length+1):
        if length == 1:
            pel[i][i] = 1
            continue   
        elif length == 2 and nlist[i] == nlist[i+1]:
            pel[i][i+1] = 1
            continue 
        if nlist[i] == nlist[i+length-1] and pel[i+1][i+length-2]:
            pel[i][i+length-1] = 1
q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(pel[x-1][y-1])