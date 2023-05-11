def solution(s):
    stack = []
    if s[0] == ")":
        return False
    for i in s:
        if not stack or i == "(":
            stack.append(i)
        else:
            if stack[-1] == "(":
                stack.pop()
    if stack:
        return False
    return True