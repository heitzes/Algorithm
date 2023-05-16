from itertools import permutations
def solution(k, dungeons):
    answer = -1
    permlist = list(map(list, permutations(range(len(dungeons)),len(dungeons))))
    for perm in permlist:
        piro, cnt = k, 0
        for dind in perm:
            dungeon = dungeons[dind]
            if piro >= dungeon[0]:
                cnt += 1
                piro -= dungeon[1]
        answer = max(answer, cnt)    
    return answer