n, m = map(int, input().split())
nlist = list(map(int, input().split()))
cnt, lo, hi = 0, 0, 0
answer = 0
while True:
    if cnt >= m:
        cnt -= nlist[lo]
        lo += 1
    elif hi == n: break
    else:
        cnt += nlist[hi]
        hi += 1
    if cnt == m: answer += 1
print(answer)