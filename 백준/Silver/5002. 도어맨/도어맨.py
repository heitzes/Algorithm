n = int(input())
order = list(input())[::-1]
cnt = [0, 0]
while order:
    flag = True
    if order[-1] == 'M':
        if abs(cnt[0]+1 - cnt[1]) <= n:
            cnt[0] += 1
            flag = False
    else:
        if abs(cnt[0] - (cnt[1]+1)) <= n:
            cnt[1] += 1
            flag = False
    if not flag: 
        order.pop()
        continue
    if len(order) >= 2:
        if order[-2] == 'M':
            if abs(cnt[0]+1 - cnt[1]) <= n:
                cnt[0] += 1
            else: break
        else:
            if abs(cnt[0] - (cnt[1]+1)) <= n:
                cnt[1] += 1
            else: break
        order.pop(-2)
    else:
        break
print(sum(cnt))