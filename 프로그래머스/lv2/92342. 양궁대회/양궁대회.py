from itertools import product
def solution(n, info):
    answer = [0] * 11
    comp = -1
    peach = set([i for i in range(11) if info[10-i] > 0])
    cnt = 0
    perm = list(map(list, product(range(2), repeat=11)))
    for p in perm:
        use = 0
        lion = set([i for i in range(11) if p[i] == 1])
        xlion = lion - peach
        xpeach = peach - lion
        lp = lion & peach
        use = len(xlion) + sum([info[10-i] + 1 if i!=0 else 0 for i in lp])
        point = sum(xlion) + sum([i for i in lp])
        diff = point - sum(xpeach)
        if use > n or diff <= 0: continue
        if diff >= comp:
            comp = diff
            ref = [0] * 11
            for i in lion:
                if i == 0: ref[10] = n - use
                elif i in lp: ref[10-i] = info[10-i] + 1
                else: ref[10-i] = 1
            for i in range(11):
                if answer[10-i] < ref[10-i]:
                    answer = ref
                    break
    if sum(answer) == 0: answer = [-1]
    return answer