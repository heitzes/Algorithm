from collections import deque
def solution(people, limit):
    answer, ind = 0, 0
    people = sorted(people)
    heavy = deque(people[::-1])
    while len(heavy) > 1:
        w = heavy.popleft()
        if w + people[ind] <= limit:
            ind += 1
            heavy.pop()
        answer += 1
    return answer + len(heavy)