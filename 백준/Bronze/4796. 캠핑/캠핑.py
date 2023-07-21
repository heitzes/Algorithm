cnt = 1
while True:
    l, p, v = map(int, input().split())
    if l==0 and p == 0 and v == 0:
        break
    k = (v) // p
    answer = (l*k) + min(v - (k*p), l)
    print("Case {}: {}".format(cnt, answer))
    cnt += 1