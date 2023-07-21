from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    score = defaultdict(int)
    for n, y in zip(name, yearning):
        score[n] = y
    for group in photo:
        answer.append(sum([score[n] for n in group]))
    return answer