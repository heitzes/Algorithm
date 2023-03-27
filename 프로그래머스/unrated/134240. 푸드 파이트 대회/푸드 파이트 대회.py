from collections import deque

def solution(food):
    align = deque(["0"])
    for i in range(len(food) - 1, 0, -1):
        it = food[i] // 2
        for _ in range(it):
            align.appendleft(str(i))
        for _ in range(it):
            align.append(str(i))

    return "".join(align)