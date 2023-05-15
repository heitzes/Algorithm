def solution(numbers):
    answer = ''
    changed = []
    for n in numbers:
        ch = (str(n) * (4))[:4]
        changed.append([ch, 4-len(str(n))])
    changed = sorted(changed, reverse=True)
    for ch, ind in changed:
        answer += ch[:4-ind]
    return str(int(answer))