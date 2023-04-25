from collections import defaultdict
def solution(keymap, targets):
    answer = []
    count = dict()
    for key in keymap:
        for i, k in enumerate(key):
            count[k] = min(count[k], i+1) if k in count else i+1
    
    for target in targets:
        cnt = 0
        for w in target:
            if w not in count:
                answer.append(-1)
                break
            cnt += count[w]
        else:
            answer.append(cnt)

    return answer