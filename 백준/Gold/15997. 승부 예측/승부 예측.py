from collections import defaultdict
from itertools import product
countries = input().split()
games = [input().split() for _ in range(6)]
ans = defaultdict(int)

def same_score(order, ans, p):
    if len(order) == 4:
        ans[order[0][1][0]] += 1 * p
        ans[order[1][1][0]] += 1 * p
    elif len(order) == 3: 
        if len(order[0][1]) == 1:
            ans[order[0][1][0]] += 1 * p
            if len(order[1][1]) == 2: # 1,2,1
                ans[order[1][1][0]] += 0.5 * p
                ans[order[1][1][1]] += 0.5 * p
            else: # 1,1,2
                ans[order[1][1][0]] += 1 * p
        else: # 2,1,1
            ans[order[0][1][0]] += 1 * p
            ans[order[0][1][1]] += 1 * p
    elif len(order) == 2:
        if len(order[0][1]) == 1: # 1,3
            ans[order[0][1][0]] += 1 * p
            ans[order[1][1][0]] += 1/3 * p
            ans[order[1][1][1]] += 1/3 * p
            ans[order[1][1][2]] += 1/3 * p
        elif len(order[0][1]) == 3: # 3, 1
            ans[order[0][1][0]] += 2/3 * p
            ans[order[0][1][1]] += 2/3 * p
            ans[order[0][1][2]] += 2/3 * p
        else: # 2, 2
            ans[order[0][1][0]] += p
            ans[order[0][1][1]] += p
    else: # 4
        ans[order[0][1][0]] += 0.5 * p
        ans[order[0][1][1]] += 0.5 * p
        ans[order[0][1][2]] += 0.5 * p
        ans[order[0][1][3]] += 0.5 * p
    return ans

for match in product(range(3), range(3), range(3), range(3), range(3), range(3)):
    percent = 1
    wins = defaultdict(int)
    for ind, v in enumerate(match):
        percent *= float(games[ind][2+v])
        if v == 0:
            wins[games[ind][0]] += 3
            wins[games[ind][1]] += 0
        elif v == 1:
            wins[games[ind][0]] += 1
            wins[games[ind][1]] += 1
        else:
            wins[games[ind][0]] += 0
            wins[games[ind][1]] += 3
    refs = defaultdict(list)
    if percent != 0.0:
        for k, v in wins.items():
            refs[v].append(k)
        order = sorted(list(refs.items()), reverse=True)
        ans = same_score(order, ans, percent)
for country in countries:
    print(ans[country])