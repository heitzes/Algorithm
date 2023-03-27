def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if i & 0xf not in [0, 1, 4, 9]:
            answer += i
        else:
            if int(i ** .5) ** 2 != i:
                answer += i
            else:
                answer -= i
    return answer