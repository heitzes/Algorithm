from collections import defaultdict
countries = input().split()
games = [input().split() for _ in range(6)]
scores = defaultdict(int)
ans = defaultdict(int)

def same_score(order, p):
    global ans
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

def find():
    global scores
    refs = defaultdict(list)
    for k, v in scores.items():
        refs[v].append(k)
    order = sorted(list(refs.items()), reverse=True)
    return order

def dfs(ind, all):
    global games, scores, ans
    if ind == 6:
        if all != 0.0:
            order = find()
            same_score(order, all)
        return

    # 이김
    scores[games[ind][0]] += (3 if ind != -1 else 0)
    scores[games[ind][1]] += (0 if ind != -1 else 0)
    dfs(ind+1, all * float(games[ind][2] if ind != -1 else 1))
    scores[games[ind][0]] -= (3 if ind != -1 else 0)

    # 비김
    scores[games[ind][0]] += (1 if ind != -1 else 0)
    scores[games[ind][1]] += (1 if ind != -1 else 0)
    dfs(ind+1, all * float(games[ind][3] if ind != -1 else 1))
    scores[games[ind][0]] -= (1 if ind != -1 else 0)
    scores[games[ind][1]] -= (1 if ind != -1 else 0)

    # 짐
    scores[games[ind][0]] += (0 if ind != -1 else 0)
    scores[games[ind][1]] += (3 if ind != -1 else 0)
    dfs(ind+1, all * float(games[ind][4] if ind != -1 else 1))
    scores[games[ind][1]] -= (3 if ind != -1 else 0)


dfs(-1, 1)
for country in countries:
    print(ans[country] / 3) # dfs(-1, 1) 때문에 dfs(0, 1)이 3번 진행됨 