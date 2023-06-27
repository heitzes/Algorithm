from bisect import bisect_left, bisect_right
n = int(input())
nlist = sorted(list(map(int, input().split())))
m = int(input())
mlist = list(map(int, input().split()))
answer = []
for num in mlist:
    if bisect_left(nlist, num) == bisect_right(nlist,num):
        answer.append('0')
    else:
        answer.append('1')
print(' '.join(answer))