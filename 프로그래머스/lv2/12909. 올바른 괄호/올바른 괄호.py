def solution(s):
    answer = True
    stack = []
    # ) 는 넣지 않고, (가 있으면 pop
    for i in s:
        if i =='(':
            stack.append(i)
        elif stack and stack[-1] == '(':
            stack.pop()
        else:
            return False
    if stack:
        return False
    return True