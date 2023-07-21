import math
from itertools import product, permutations
def solution(picks, minerals):
    """
    반복 종료 조건; 곡괭이 없거나 모든 광물 캠
    요구 사항; 하나의 곡괭이의 목숨은 5개(목숨 없어지거나 광물 없을때까지 써야함)
    
    1. 사용할 곡괭이의 갯수
        -> math.ceil(미네랄 수 / 5)
        -> 최대 곡갱이는 15개, 최대 필요한 곡괭이는 10개
        -> 곡괭이 갯수 (다, 철, 돌) 순열로 구하고 완전탐색
    2. 곡괭이의 배치
        -> (2,1,1)에 대해 다다철돌/다철돌다/.. 이런식으로 사용할 수 있음
        -> 완전탐색으로 최소 피로도 구할거임
    """
    
    answer = 1e9
    needs = math.ceil(len(minerals) / 5)
    combination = [p for p in product(range(picks[0]+1), range(picks[1]+1), range(picks[2]+1)) if sum(p)==min(sum(picks), needs)]
    pirodo = [[1,1,1], [5,1,1], [25,5,1]]
    translate = {"diamond": 0, "iron": 1, "stone": 2}

    for comb in combination:
        gang = [0]*comb[0]+[1]*comb[1]+[2]*comb[2]
        permutation = set(permutations(gang,sum(comb)))
        for perm in permutation:
            cnt, piro = 0, 0
            for g in perm:
                for mineral in minerals[cnt:cnt+5]:
                    piro += pirodo[g][translate[mineral]]
                cnt += 5
            answer = min(answer, piro)
    return answer