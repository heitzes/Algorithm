def solution(numbers):
    answer = []
    stack = []
    
    for num in numbers[::-1]:
        while stack:
            if stack[-1] > num:
                answer.append(stack[-1])
                stack.append(num)
                break
            stack.pop()
        if not stack:
            answer.append(-1)
            stack.append(num)
    
    return answer[::-1]