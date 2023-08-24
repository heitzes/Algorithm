def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:
        newsk = ''
        for s in sk:
            if s in skill: newsk += s
        if newsk == skill[:len(newsk)]: answer += 1
    return answer