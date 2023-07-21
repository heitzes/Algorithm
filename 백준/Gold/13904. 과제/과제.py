from bisect import bisect_right
n = int(input())
hwlist = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: -x[1])
dp = [0] * (max(hwlist)[0]+1)
done, idone = [], []
for ind, hw in enumerate(hwlist):
    day, val = hw[0], hw[1:]
    done = sorted(done)
    if bisect_right(done, day) >= day: continue
    for i in range(day+1, done[-1]+1 if done else 0):
        cnt = bisect_right(done, i)
        if cnt + 1 > i: break
    else:
        done.append(day)
        idone.append(ind)
print(sum([hwlist[i][-1] for i in idone]))