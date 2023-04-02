from collections import deque
def check(string):
    dq = deque(list(string))
    index = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3}
    open_str = ['(', '[', '{']
    stack = [dq.popleft()]
    while dq:
        spop = dq.popleft()
        if stack:
            # 실수: index[stack[-1]] == index[spop]로 하면 '(' == '(' 도 해당 됨!
            if not (index[stack[-1]] + index[spop]) and stack[-1] in open_str:
                stack.pop()
                continue
        stack.append(spop)
    if stack:
        return 0
    return 1
def solution(s):
    ind, cnt = 1, check(s)
    while ind < len(s):
        s = s[1:] + s[0]
        cnt += check(s)
        ind += 1
    return cnt