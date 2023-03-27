def solution(babbling):
    def check(b):
        prev = b[0]
        if prev.isalpha():
            return False
        for i in range(1, len(b)):
            if b[i].isalpha():
                return False
            if prev == b[i]:
                return False
            prev = b[i]
        return True
        
    answer = 0
    patterns = {"aya": "^", "ye": "&", "woo": "*", "ma": "$"}
    for b in babbling:
        for p in patterns:
            b = b.replace(p, patterns[p])
        if check(b):
            answer += 1
    return answer