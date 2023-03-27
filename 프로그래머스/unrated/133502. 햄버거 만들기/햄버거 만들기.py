def solution(ingredient):
    def check():
        for i in range(1, 5):
            if stack[-i] != pattern[-i]:
                return False
        return True

    answer = 0
    pattern = [1, 2, 3, 1]
    stack = []
    for i in ingredient:
        if len(stack) < 4:
            stack.append(i)
            continue
        
        if check():
            answer += 1
            for _ in range(4):
                stack.pop()
        stack.append(i)
    
    if len(stack) >= 4 and check():
        answer += 1

    return answer

