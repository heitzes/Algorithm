def solution(s):
    answer = 0
    start = 0
    while start < len(s):
        ch = s[start]
        comp = [1, 0]
        ind = start + 1
        while comp[0] != comp[1]:
            if ind == len(s):
                break
            if ch == s[ind]:
                comp[0] += 1
            else:
                comp[1] += 1
            ind += 1
        start = ind
        answer += 1
            
    return answer