from collections import defaultdict
def solution(genres, plays):
    answer = []
    # 1. {장르1: [[재생수, 번호]], 장르2: [[재생수, 번호]]} 순으로 정리
    # 2. {장르1: 총 재생수} 순으로 정리
    glist = defaultdict(int)
    gdict = defaultdict(list)
    for i, p in enumerate(plays):
        g = genres[i]
        glist[g] += p
        gdict[g].append([p, i])
    gorder = sorted(list(glist.items()), key=lambda x: -x[1])
    for g, _ in gorder:
        gplay = sorted(gdict[g], key=lambda x: (-x[0], x[1]))
        answer.extend([i[1] for i in gplay[:2]])
    return answer