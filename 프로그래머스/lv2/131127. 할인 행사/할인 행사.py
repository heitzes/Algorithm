from collections import Counter
def solution(want, number, discount):
    answer = 0
    count = Counter(discount[:10])
    needs = set(zip(want, number))
    if needs.issubset(set(count.items())):
        answer += 1
    for i in range(10, len(discount)):
        count[discount[i]] += 1
        count[discount[i-10]] -= 1
        if needs.issubset(set(count.items())):
            answer += 1
    return answer