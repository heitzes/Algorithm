def solution(numbers):
    answer = ''
    changed = []
    for n in numbers:
        ch = (str(n) * (4))[:4]
        changed.append([ch, len(str(n))])
    changed = sorted(changed, reverse=True)
    for ch, ind in changed:
        answer += ch[:ind]
    return str(int(answer))