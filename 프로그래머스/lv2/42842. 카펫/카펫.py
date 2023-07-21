def solution(brown, yellow):
    answer = []
    av = brown + yellow
    for n in range(1, int(av**0.5)+1):
        if (av / n) % 1 != 0.0:
            continue
        if brown == 2*n + 2*(av/n) - 4:
            return [int(av/n), n]
    return answer