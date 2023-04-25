def solution(s):
    answer = 0
    same, diff = 0, 0
    for i in s:
        if same == diff:
            answer += 1
            ch = i
        if i == ch:
            same += 1
        else:
            diff += 1
    return answer