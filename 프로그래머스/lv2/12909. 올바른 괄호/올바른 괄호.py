def solution(s):
    stack = []
    for i in s:
        if not stack or i == '(':
            stack.append(i)
            continue
        if stack[-1] == '(':
            stack.pop()
    return len(stack) == 0