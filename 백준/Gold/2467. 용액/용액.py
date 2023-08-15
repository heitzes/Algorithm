from bisect import bisect_left
n = int(input())
nlist = list(map(int, input().split()))
answer = float('inf')
x, y = 0, 0
def compare(a, b, new):
    global x, y, answer
    if new < answer:
        answer = new
        x, y = a, b 
for idx, i in enumerate(nlist):
    ind = bisect_left(nlist, i*(-1))
    if ind == n: 
        if idx != n-1:
            compare(idx, n-1, abs(i+nlist[n-1]))
        continue
    if idx != ind:
        compare(idx, ind, abs(i+nlist[ind]))
    if ind - 1 >= 0 and idx != ind-1:
        compare(idx, ind-1, abs(i+nlist[ind-1]))
    if ind + 1 < n and idx != ind+1:
        compare(idx, ind+1, abs(i+nlist[ind+1]))
print(nlist[x], nlist[y])