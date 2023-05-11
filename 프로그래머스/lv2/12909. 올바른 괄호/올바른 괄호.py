def solution(s):
    stack = []
    if s[0] == ")":
        return False
    for i in s:
        if not stack or i == "(":
            stack.append(i)
        else:
            stack.pop()
    return len(stack) == 0