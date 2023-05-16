from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while len(people) > 1:
        w = people.pop()
        if w + people[0] <= limit:
            people.popleft()
        answer += 1
    return answer + len(people)